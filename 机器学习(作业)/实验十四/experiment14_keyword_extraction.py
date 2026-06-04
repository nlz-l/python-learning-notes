"""
实验十四：新闻语料关键词提取对比

使用 20 Newsgroups 英文新闻语料完成关键词提取算法比较。
算法仍基于原始英文 token 计算，结果展示时转换为中文释义，便于中文实验报告使用。
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer


BASE_DIR = Path(__file__).resolve().parent
CORPUS_PATH = BASE_DIR / "新闻语料_20类新闻.csv"
RESULT_PATH = BASE_DIR / "关键词提取结果对比.csv"
OVERLAP_PATH = BASE_DIR / "关键词重合度矩阵.csv"
PLOT_PATH = BASE_DIR / "关键词提取算法对比图.png"

RANDOM_STATE = 42
TOP_N = 15

KEYWORD_ZH = {
    "space": "太空",
    "israel": "以色列",
    "israeli": "以色列人",
    "armenians": "亚美尼亚人",
    "armenian": "亚美尼亚",
    "turkish": "土耳其",
    "nasa": "美国航天局",
    "ftp": "文件传输",
    "program": "程序",
    "graphics": "图形",
    "image": "图像",
    "file": "文件",
    "files": "文件",
    "data": "数据",
    "base": "棒球垒",
    "year": "年份",
    "years": "年份",
    "said": "表示",
    "say": "说",
    "came": "出现",
    "way": "方式",
    "problem": "问题",
    "went": "前往",
    "won": "获胜",
    "lost": "失利",
    "available": "可用",
    "soldiers": "士兵",
    "edu": "教育域名",
    "need": "需要",
    "better": "更好",
    "thanks": "感谢",
    "game": "比赛",
    "team": "球队",
    "games": "赛事",
    "players": "球员",
    "baerga": "贝尔加",
    "alomar": "阿洛马",
    "launch": "发射",
    "orbit": "轨道",
    "moon": "月球",
    "earth": "地球",
}


def to_zh_keyword(word: str) -> str:
    return KEYWORD_ZH.get(word, word)


def download_news_corpus() -> pd.DataFrame:
    if CORPUS_PATH.exists():
        df = pd.read_csv(CORPUS_PATH)
        if {"category", "text"}.issubset(df.columns):
            print(f"发现本地语料缓存：{CORPUS_PATH.name}，共 {len(df)} 篇文档")
            return df
        print(f"发现旧缓存缺少必要列，重新下载：{CORPUS_PATH.name}")

    categories = [
        "sci.space",
        "rec.sport.baseball",
        "talk.politics.mideast",
        "comp.graphics",
    ]
    dataset = fetch_20newsgroups(
        subset="train",
        categories=categories,
        remove=("headers", "footers", "quotes"),
        shuffle=True,
        random_state=RANDOM_STATE,
    )
    df = pd.DataFrame(
        {
            "category": [dataset.target_names[i] for i in dataset.target],
            "text": dataset.data,
        }
    )

    sampled_parts = []
    for category in categories:
        part = df[df["category"] == category]
        sampled_parts.append(part.sample(min(45, len(part)), random_state=RANDOM_STATE))
    df = pd.concat(sampled_parts, ignore_index=True)
    df.to_csv(CORPUS_PATH, index=False, encoding="utf-8-sig")
    print(f"语料已保存：{CORPUS_PATH.name}，共 {len(df)} 篇文档")
    return df


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z-]{2,}", str(text).lower())
    stop_words = set(ENGLISH_STOP_WORDS)
    stop_words.update(
        {
            "article",
            "writes",
            "subject",
            "lines",
            "organization",
            "people",
            "know",
            "think",
            "just",
            "like",
            "does",
            "did",
            "use",
            "used",
            "using",
            "time",
            "good",
            "new",
            "don",
            "didn",
            "doesn",
            "isn",
            "aren",
            "wasn",
            "weren",
            "can",
            "could",
        }
    )
    return [word for word in tokens if word not in stop_words and len(word) >= 3]


def build_documents(df: pd.DataFrame) -> tuple[list[list[str]], list[str]]:
    token_docs = [tokenize(text) for text in df["text"]]
    token_docs = [tokens for tokens in token_docs if len(tokens) >= 10]
    docs = [" ".join(tokens) for tokens in token_docs]
    print(f"停用词过滤后保留 {len(docs)} 篇有效文档")
    print(f"总词数：{sum(len(tokens) for tokens in token_docs):,}")
    print(f"不同词数：{len(set(word for tokens in token_docs for word in tokens)):,}")
    return token_docs, docs


def extract_tfidf_keywords(docs: list[str], top_n: int = TOP_N) -> pd.DataFrame:
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.85, max_features=2000)
    tfidf = vectorizer.fit_transform(docs)
    terms = np.array(vectorizer.get_feature_names_out())
    scores = np.asarray(tfidf.mean(axis=0)).ravel()
    order = scores.argsort()[::-1][:top_n]
    return pd.DataFrame(
        {"algorithm": "TF-IDF", "rank": range(1, top_n + 1), "keyword": terms[order], "score": scores[order]}
    )


def extract_textrank_keywords(token_docs: list[list[str]], top_n: int = TOP_N) -> pd.DataFrame:
    word_freq = Counter(word for tokens in token_docs for word in tokens)
    vocab = {word for word, _ in word_freq.most_common(900) if word_freq[word] >= 2}
    graph: dict[str, Counter[str]] = defaultdict(Counter)

    for tokens in token_docs:
        filtered = [word for word in tokens if word in vocab]
        for i, word in enumerate(filtered):
            for other in filtered[i + 1 : i + 4]:
                if word == other:
                    continue
                graph[word][other] += 1
                graph[other][word] += 1

    scores = {word: 1.0 for word in graph}
    out_weight = {word: sum(neighbors.values()) for word, neighbors in graph.items()}
    damping = 0.85

    for _ in range(60):
        new_scores = {}
        max_delta = 0.0
        for word, neighbors in graph.items():
            rank_sum = 0.0
            for other, weight in neighbors.items():
                rank_sum += scores[other] * weight / out_weight[other]
            new_score = (1 - damping) + damping * rank_sum
            new_scores[word] = new_score
            max_delta = max(max_delta, abs(new_score - scores[word]))
        scores = new_scores
        if max_delta < 1e-5:
            break

    top_items = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:top_n]
    return pd.DataFrame(
        {
            "algorithm": "TextRank",
            "rank": range(1, len(top_items) + 1),
            "keyword": [word for word, _ in top_items],
            "score": [score for _, score in top_items],
        }
    )


def extract_lsa_keywords(docs: list[str], top_n: int = TOP_N) -> pd.DataFrame:
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.85, max_features=2000)
    tfidf = vectorizer.fit_transform(docs)
    terms = np.array(vectorizer.get_feature_names_out())
    n_components = min(6, tfidf.shape[1] - 1)
    svd = TruncatedSVD(n_components=n_components, random_state=RANDOM_STATE)
    svd.fit(tfidf)
    topic_weights = svd.explained_variance_ratio_
    scores = np.sum(np.abs(svd.components_) * topic_weights[:, np.newaxis], axis=0)
    order = scores.argsort()[::-1][:top_n]
    return pd.DataFrame(
        {"algorithm": "LSA", "rank": range(1, top_n + 1), "keyword": terms[order], "score": scores[order]}
    )


def compare_overlap(result: pd.DataFrame) -> pd.DataFrame:
    keyword_sets = {alg: set(group["keyword"]) for alg, group in result.groupby("algorithm")}
    rows = []
    for left in keyword_sets:
        row = {right: len(keyword_sets[left] & keyword_sets[right]) for right in keyword_sets}
        row["算法"] = left
        rows.append(row)
    return pd.DataFrame(rows).set_index("算法")


def enrich_result(result: pd.DataFrame) -> pd.DataFrame:
    result = result.copy()
    result["keyword_zh"] = result["keyword"].map(to_zh_keyword)
    result = result.rename(
        columns={
            "algorithm": "算法",
            "rank": "排名",
            "keyword": "英文关键词",
            "keyword_zh": "中文关键词",
            "score": "得分",
        }
    )
    return result[["算法", "排名", "英文关键词", "中文关键词", "得分"]]


def plot_keywords(result: pd.DataFrame) -> None:
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, axes = plt.subplots(1, 3, figsize=(15, 6), constrained_layout=True)
    colors = {"TF-IDF": "#2F7D8C", "TextRank": "#C45A3A", "LSA": "#6A8E3B"}

    for ax, algorithm in zip(axes, ["TF-IDF", "TextRank", "LSA"]):
        data = result[result["algorithm"] == algorithm].head(10).iloc[::-1]
        normalized = data["score"] / data["score"].max()
        labels = data["keyword"].map(to_zh_keyword)
        ax.barh(labels, normalized, color=colors[algorithm])
        ax.set_title(f"{algorithm} 关键词")
        ax.set_xlabel("归一化得分")
        ax.grid(axis="x", linestyle="--", alpha=0.25)

    fig.suptitle("20 Newsgroups 新闻语料关键词提取算法对比", fontsize=14)
    fig.savefig(PLOT_PATH, dpi=180)
    print(f"中文对比图已保存：{PLOT_PATH.name}")


def main() -> None:
    df = download_news_corpus()
    print("\n===== 语料类别分布 =====")
    print(df["category"].value_counts().to_string())

    token_docs, docs = build_documents(df)
    result = pd.concat(
        [
            extract_tfidf_keywords(docs),
            extract_textrank_keywords(token_docs),
            extract_lsa_keywords(docs),
        ],
        ignore_index=True,
    )
    result_zh = enrich_result(result)
    overlap = compare_overlap(result)

    result_zh.to_csv(RESULT_PATH, index=False, encoding="utf-8-sig")
    overlap.to_csv(OVERLAP_PATH, encoding="utf-8-sig")
    plot_keywords(result)

    print("\n===== 三种算法 Top 15 中文关键词 =====")
    print(result_zh.pivot(index="排名", columns="算法", values="中文关键词").to_string())
    print("\n===== Top 15 关键词重合数量 =====")
    print(overlap.to_string())


if __name__ == "__main__":
    main()
