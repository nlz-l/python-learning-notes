from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
OUT_DIR = BASE_DIR / "output"
FIG_DIR = OUT_DIR / "figures"

DATASETS = {
    "china_nev_sales": {
        "url": "https://chinadata.live/api/v2/data/china-nev-sales",
        "name": "中国新能源汽车年度销量",
        "source": "中国汽车工业协会 CAAM",
    },
    "china_car_production_monthly": {
        "url": "https://chinadata.live/api/v2/data/china-car-production-monthly",
        "name": "中国汽车月度产量",
        "source": "国家统计局 NBS",
    },
    "ev_sales_china_vs_world": {
        "url": "https://chinadata.live/api/v2/data/ev-sales-china-vs-world",
        "name": "中国与全球电动汽车销量对比",
        "source": "IEA、EV-Volumes、中国汽车工业协会",
    },
}


def setup_plot_style() -> None:
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False
    sns.set_theme(style="whitegrid", font="SimHei")


def fetch_dataset(key: str) -> tuple[pd.DataFrame, dict]:
    meta = DATASETS[key]
    response = requests.get(meta["url"], timeout=60)
    response.raise_for_status()
    payload = response.json()["data"]
    df = pd.DataFrame(payload["data"])
    raw_path = OUT_DIR / f"raw_{key}.csv"
    df.to_csv(raw_path, index=False, encoding="utf-8-sig")
    return df, payload


def missing_table(df: pd.DataFrame, label: str) -> pd.DataFrame:
    return (
        pd.DataFrame(
            {
                "stage": label,
                "column": df.columns,
                "missing_count": df.isna().sum().values,
                "missing_rate": (df.isna().mean().values * 100).round(2),
            }
        )
        .sort_values(["missing_count", "column"], ascending=[False, True])
        .reset_index(drop=True)
    )


def profile_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col in df.columns:
        rows.append(
            {
                "column": col,
                "dtype": str(df[col].dtype),
                "non_null_count": int(df[col].notna().sum()),
                "missing_count": int(df[col].isna().sum()),
                "unique_count": int(df[col].nunique(dropna=True)),
            }
        )
    return pd.DataFrame(rows)


def cap_by_iqr(series: pd.Series) -> tuple[pd.Series, float, float, int]:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = max(0, q1 - 1.5 * iqr)
    upper = q3 + 1.5 * iqr
    mask = (series < lower) | (series > upper)
    return series.clip(lower, upper), round(lower, 4), round(upper, 4), int(mask.sum())


def clean_monthly_production(raw: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, object]], dict[str, object]]:
    log: list[dict[str, object]] = []
    df = raw.copy()
    df.columns = ["date", "production_10k"]
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m")
    df["production_10k"] = pd.to_numeric(df["production_10k"], errors="coerce")
    df = df.drop_duplicates(subset=["date"]).sort_values("date")
    log.append({"step": "字段规范化", "detail": "将月度产量字段统一为 date、production_10k，并转换日期类型。"})

    full_months = pd.DataFrame({"date": pd.date_range(df["date"].min(), df["date"].max(), freq="MS")})
    clean = full_months.merge(df, on="date", how="left")
    clean["year"] = clean["date"].dt.year
    clean["month"] = clean["date"].dt.month
    clean["quarter"] = clean["date"].dt.quarter
    clean["production_missing_flag"] = clean["production_10k"].isna().astype(int)
    inserted_missing = int(clean["production_missing_flag"].sum())
    log.append({"step": "补全时间索引", "detail": f"按完整月份序列补齐时间索引，新增 {inserted_missing} 条原始未报告月份。"})

    month_median = clean.groupby("month")["production_10k"].transform("median")
    clean["production_filled_10k"] = clean["production_10k"].fillna(month_median).fillna(clean["production_10k"].median())
    log.append({"step": "缺失值处理", "detail": "汽车月度产量缺失值使用同月历史中位数填补，保留 production_missing_flag 标记。"})

    clean["production_before_cap_10k"] = clean["production_filled_10k"]
    clean["production_filled_10k"], low, high, outliers = cap_by_iqr(clean["production_filled_10k"])
    clean["production_filled_10k"] = clean["production_filled_10k"].round(2)
    clean["production_10k"] = clean["production_10k"].fillna(clean["production_filled_10k"]).round(2)
    log.append({"step": "异常值处理", "detail": f"使用 IQR 检查月度产量异常值，截尾范围 [{low}, {high}]，调整 {outliers} 个值。"})

    clean["production_yoy"] = clean["production_filled_10k"].pct_change(12).replace([np.inf, -np.inf], np.nan)
    clean["production_yoy"] = clean["production_yoy"].fillna(0).round(4)
    clean["production_level"] = pd.qcut(
        clean["production_filled_10k"].rank(method="first"),
        q=4,
        labels=["低产量", "中低产量", "中高产量", "高产量"],
    )
    clean["month_name"] = clean["month"].astype(str).str.zfill(2) + "月"
    log.append({"step": "特征构造", "detail": "新增 year、month、quarter、production_yoy、production_level 等时间序列分析字段。"})

    stats = {"production_iqr_low": low, "production_iqr_high": high, "production_outliers": outliers, "inserted_missing_months": inserted_missing}
    return clean, log, stats


def clean_annual_nev(raw_nev: pd.DataFrame, raw_compare: pd.DataFrame, monthly: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    log: list[dict[str, object]] = []
    nev = raw_nev.copy()
    nev.columns = ["year", "nev_sales_10k"]
    nev["year"] = pd.to_numeric(nev["year"], errors="coerce").astype(int)
    nev["nev_sales_10k"] = pd.to_numeric(nev["nev_sales_10k"], errors="coerce")
    nev = nev.drop_duplicates(subset=["year"]).sort_values("year")
    log.append({"step": "年度销量字段规范化", "detail": "新能源汽车年度销量字段统一为 year、nev_sales_10k，单位为万辆。"})

    comp = raw_compare.copy()
    comp["year"] = pd.to_numeric(comp["date"], errors="coerce").astype(int)
    comp = comp.drop(columns=["date"])
    for col in ["china", "world_total", "world_minus_china", "china_share"]:
        comp[col] = pd.to_numeric(comp[col], errors="coerce")
    comp = comp.rename(
        columns={
            "china": "china_ev_sales_million",
            "world_total": "world_ev_sales_million",
            "world_minus_china": "world_minus_china_million",
            "china_share": "china_world_share_pct",
        }
    )
    log.append({"step": "全球对比字段规范化", "detail": "中国与全球电动车销量对比数据统一为年度字段，并保留中国全球占比。"})

    annual_prod = (
        monthly.groupby("year", as_index=False)
        .agg(
            car_production_10k=("production_filled_10k", "sum"),
            reported_months=("production_missing_flag", lambda s: int((s == 0).sum())),
            filled_months=("production_missing_flag", "sum"),
        )
        .round({"car_production_10k": 2})
    )

    annual = nev.merge(annual_prod, on="year", how="left").merge(comp, on="year", how="left")
    annual["nev_sales_million"] = (annual["nev_sales_10k"] / 100).round(4)
    annual["nev_sales_yoy"] = annual["nev_sales_10k"].pct_change().round(4)
    annual["nev_to_car_output_ratio_pct"] = (annual["nev_sales_10k"] / annual["car_production_10k"] * 100).round(2)
    annual["policy_stage"] = pd.cut(
        annual["year"],
        bins=[2010, 2015, 2020, 2025],
        labels=["示范推广期", "补贴调整期", "规模化增长期"],
        include_lowest=True,
    )
    annual["china_world_share_pct"] = annual["china_world_share_pct"].fillna(
        (annual["nev_sales_million"] / annual["world_ev_sales_million"] * 100).round(1)
    )
    log.append({"step": "年度特征构造", "detail": "合并年度销量、汽车产量和全球对比数据，新增同比增速、渗透率代理指标和政策阶段。"})

    annual = annual.fillna(
        {
            "china_ev_sales_million": 0,
            "world_ev_sales_million": 0,
            "world_minus_china_million": 0,
            "china_world_share_pct": 0,
            "nev_sales_yoy": 0,
        }
    )
    return annual, log


def save_figures(monthly: pd.DataFrame, annual: pd.DataFrame, missing_before: pd.DataFrame, missing_after: pd.DataFrame) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    merged_missing = pd.concat([missing_before, missing_after], ignore_index=True)
    plt.figure(figsize=(9, 5))
    sns.barplot(data=merged_missing, x="column", y="missing_count", hue="stage")
    plt.title("补齐月份后填补前与清洗后缺失值对比")
    plt.xlabel("字段")
    plt.ylabel("缺失值数量")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "01_missing_before_after.png", dpi=200)
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=annual, x="year", y="nev_sales_10k", marker="o", color="#2ca25f")
    plt.title("中国新能源汽车年度销量趋势")
    plt.xlabel("年份")
    plt.ylabel("销量（万辆）")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02_nev_sales_trend.png", dpi=200)
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=annual, x="year", y="nev_sales_yoy", color="#3182bd")
    plt.axhline(0, color="#666666", linewidth=1)
    plt.title("中国新能源汽车年度销量同比增速")
    plt.xlabel("年份")
    plt.ylabel("同比增速")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "03_nev_yoy_growth.png", dpi=200)
    plt.close()

    plt.figure(figsize=(11, 5))
    sns.lineplot(data=monthly, x="date", y="production_filled_10k", color="#756bb1")
    plt.title("中国汽车月度产量清洗后趋势")
    plt.xlabel("月份")
    plt.ylabel("产量（万辆）")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "04_monthly_car_production.png", dpi=200)
    plt.close()

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.boxplot(y=monthly["production_10k"], ax=axes[0], color="#9ecae1")
    axes[0].set_title("原始月度产量")
    axes[0].set_ylabel("万辆")
    sns.boxplot(y=monthly["production_filled_10k"], ax=axes[1], color="#74c476")
    axes[1].set_title("清洗后月度产量")
    axes[1].set_ylabel("万辆")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "05_production_boxplot_before_after.png", dpi=200)
    plt.close()

    plt.figure(figsize=(9, 5))
    sns.lineplot(data=annual, x="year", y="china_world_share_pct", marker="o", color="#e6550d")
    plt.title("中国电动汽车销量全球占比")
    plt.xlabel("年份")
    plt.ylabel("全球占比（%）")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "06_china_world_share.png", dpi=200)
    plt.close()

    compare = annual[annual["world_ev_sales_million"] > 0]
    plt.figure(figsize=(10, 5))
    plt.plot(compare["year"], compare["china_ev_sales_million"], marker="o", label="中国")
    plt.plot(compare["year"], compare["world_minus_china_million"], marker="o", label="世界其他地区")
    plt.title("中国与世界其他地区电动汽车销量对比")
    plt.xlabel("年份")
    plt.ylabel("销量（百万辆）")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "07_china_vs_world_ev_sales.png", dpi=200)
    plt.close()

    corr_cols = ["nev_sales_10k", "car_production_10k", "nev_sales_yoy", "nev_to_car_output_ratio_pct", "china_world_share_pct"]
    plt.figure(figsize=(8, 6))
    sns.heatmap(annual[corr_cols].corr(), annot=True, fmt=".2f", cmap="RdBu_r", center=0, square=True)
    plt.title("年度新能源汽车关键指标相关系数热力图")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "08_annual_correlation_heatmap.png", dpi=200)
    plt.close()


def main() -> None:
    setup_plot_style()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_nev, meta_nev = fetch_dataset("china_nev_sales")
    raw_monthly, meta_monthly = fetch_dataset("china_car_production_monthly")
    raw_compare, meta_compare = fetch_dataset("ev_sales_china_vs_world")

    monthly, monthly_log, monthly_stats = clean_monthly_production(raw_monthly)
    monthly_before = monthly[["date", "production_10k", "year", "month", "quarter"]].copy()
    monthly_before.loc[monthly["production_missing_flag"] == 1, "production_10k"] = np.nan
    missing_before = missing_table(monthly_before, "填补前")
    raw_profile = profile_table(monthly_before)

    annual, annual_log = clean_annual_nev(raw_nev, raw_compare, monthly)
    log = monthly_log + annual_log
    missing_after = missing_table(monthly, "清洗后")
    monthly_profile = profile_table(monthly)
    annual_profile = profile_table(annual)

    monthly.to_csv(OUT_DIR / "cleaned_china_car_production_monthly.csv", index=False, encoding="utf-8-sig")
    annual.to_csv(OUT_DIR / "cleaned_china_nev_annual.csv", index=False, encoding="utf-8-sig")
    save_figures(monthly, annual, missing_before, missing_after)

    quality_summary = {
        "topic": "中国新能源汽车与汽车产量数据清洗",
        "data_source_page": "https://chinadata.live/data/china-nev-sales/",
        "nev_source": meta_nev["source"],
        "monthly_source": meta_monthly["source"],
        "comparison_source": meta_compare["source"],
        "nev_api": DATASETS["china_nev_sales"]["url"],
        "monthly_api": DATASETS["china_car_production_monthly"]["url"],
        "comparison_api": DATASETS["ev_sales_china_vs_world"]["url"],
        "nev_year_start": int(annual["year"].min()),
        "nev_year_end": int(annual["year"].max()),
        "monthly_rows_raw": int(raw_monthly.shape[0]),
        "monthly_rows_clean": int(monthly.shape[0]),
        "annual_rows_clean": int(annual.shape[0]),
        "missing_before_total": int(monthly_before.isna().sum().sum()),
        "missing_after_total": int(monthly.isna().sum().sum()),
        "inserted_missing_months": int(monthly_stats["inserted_missing_months"]),
        "latest_nev_year": int(annual["year"].max()),
        "latest_nev_sales_10k": float(annual.loc[annual["year"].idxmax(), "nev_sales_10k"]),
        "latest_nev_sales_million": float(annual.loc[annual["year"].idxmax(), "nev_sales_million"]),
        "latest_china_world_share_pct": float(annual.loc[annual["year"].idxmax(), "china_world_share_pct"]),
        "latest_nev_to_car_output_ratio_pct": float(annual.loc[annual["year"].idxmax(), "nev_to_car_output_ratio_pct"]),
        **monthly_stats,
    }

    with pd.ExcelWriter(OUT_DIR / "cleaning_summary.xlsx", engine="openpyxl") as writer:
        missing_before.to_excel(writer, sheet_name="missing_before", index=False)
        missing_after.to_excel(writer, sheet_name="missing_after", index=False)
        raw_profile.to_excel(writer, sheet_name="raw_profile", index=False)
        monthly_profile.to_excel(writer, sheet_name="monthly_profile", index=False)
        annual_profile.to_excel(writer, sheet_name="annual_profile", index=False)
        pd.DataFrame(log).to_excel(writer, sheet_name="cleaning_log", index=False)
        monthly.select_dtypes(include=[np.number]).describe().T.round(4).to_excel(writer, sheet_name="monthly_stats")
        annual.select_dtypes(include=[np.number]).describe().T.round(4).to_excel(writer, sheet_name="annual_stats")
        pd.DataFrame([quality_summary]).to_excel(writer, sheet_name="quality_summary", index=False)

    with open(OUT_DIR / "summary.json", "w", encoding="utf-8") as f:
        json.dump({"quality_summary": quality_summary, "cleaning_log": log}, f, ensure_ascii=False, indent=2)

    (OUT_DIR / "data_source.txt").write_text(
        f"主题: 中国新能源汽车与汽车产量数据清洗\n"
        f"新能源汽车年度销量 API: {DATASETS['china_nev_sales']['url']}\n"
        f"汽车月度产量 API: {DATASETS['china_car_production_monthly']['url']}\n"
        f"中国与全球电动汽车销量对比 API: {DATASETS['ev_sales_china_vs_world']['url']}\n"
        f"主要数据来源: 中国汽车工业协会、国家统计局、IEA/EV-Volumes 等公开统计口径\n",
        encoding="utf-8",
    )

    print("中国新能源汽车数据清洗完成")
    print(f"清洗后月度数据: {OUT_DIR / 'cleaned_china_car_production_monthly.csv'}")
    print(f"清洗后年度数据: {OUT_DIR / 'cleaned_china_nev_annual.csv'}")
    print(f"质量汇总: {OUT_DIR / 'cleaning_summary.xlsx'}")
    print(f"图表目录: {FIG_DIR}")


if __name__ == "__main__":
    main()
