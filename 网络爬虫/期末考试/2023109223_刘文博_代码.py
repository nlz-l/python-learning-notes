import re, time
from pathlib import Path
from urllib.parse import quote

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TARGET = 300
OUT_DIR = Path(__file__).parent / "output"
FIELDS = ["产品名称", "品牌", "功效标签", "售价", "容量规格", "成分列表",
          "用户使用评论", "source_site", "source_url"]
KEYWORDS = ["美妆护肤", "面膜", "护肤套装", "爽肤水", "精华液", "洁面乳", "防晒霜", "乳液",
            "面霜", "眼霜", "口红", "粉底液", "卸妆水", "化妆水", "洗面奶", "香水", "眉笔", "散粉"]
EFFECTS = ["保湿", "补水", "控油", "清洁", "美白", "淡斑", "修护", "抗皱", "舒缓", "提亮", "防晒"]
INGREDIENTS = ["玻尿酸", "透明质酸", "烟酰胺", "氨基酸", "B5", "水杨酸", "神经酰胺",
               "维生素", "白泥", "蜂蜜", "芦荟", "视黄醇", "胶原蛋白"]

def build_driver():
    opt = Options()
    opt.binary_location = EDGE
    opt.add_argument("--headless=new")
    opt.add_argument("--window-size=1366,900")
    opt.add_argument("--disable-gpu")
    return webdriver.Edge(options=opt)
#从产品名称中提取容量规格信息
def capacity(name):
    vals = re.findall(r"\d+(?:\.\d+)?\s?(?:ml|mL|ML|g|G|kg|片|支|瓶|盒|包|枚|色)", name)
    return "；".join(dict.fromkeys(vals))
#从产品名称中提取品牌名称
def brand(name):
    m = re.match(r"([A-Za-z0-9\u4e00-\u9fa5]+)(?:\(|（|\s)", name)
    return m.group(1) if m else name[:8]
#从关键词列表中筛选出在产品名称中出现的关键词
def pick(words, name):
    return "；".join([w for w in words if w.lower() in name.lower()])
#校验产品名称是否有效
def valid_name(name):
    bad = ["对比", "关注", "查看详情", "加入购物车", "广告"]
    return not (name.startswith("¥") or name in bad or len(name) < 8)
# 解析页面文本行，提取美妆商品数据
def parse_lines(lines, source_url):
    rows, i = [], 0
    while i < len(lines) - 3:
        if lines[i].startswith("¥"):
            price, name = lines[i], lines[i + 1]
            if not valid_name(name):
                i += 1; continue
            comment, shop = "", ""
            for x in lines[i + 2:i + 8]:
                if "评价" in x and not comment: comment = x
                elif x not in ["广告", "对比", "关注", "查看详情", "加入购物车"] and not re.search(r"券|满|折|件$", x):
                    if "评价" not in x and not shop: shop = x
            rows.append({"产品名称": name, "品牌": brand(name), "功效标签": pick(EFFECTS, name),
                         "售价": price, "容量规格": capacity(name), "成分列表": pick(INGREDIENTS, name),
                         "用户使用评论": comment, "source_site": shop or "苏宁易购",
                         "source_url": source_url})
            i += 4
        i += 1
    return rows

def main():
    driver, rows, seen = build_driver(), [], set()
    try:
        for kw in KEYWORDS:
            if len(rows) >= TARGET: break
            url = f"https://search.suning.com/{quote(kw)}/"
            # 1. 获取数据：用 Edge + Selenium 打开苏宁易购中国站美妆商品搜索页。
            driver.get(url); time.sleep(6)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            # 2. 解析数据：使用 XPath 提取页面正文，再按价格行切分商品块。
            body = driver.find_element(By.XPATH, "//body").text
            lines = [x.strip() for x in body.splitlines() if x.strip()]
            # 3. 提取数据：提取商品名、品牌、标签、价格、规格、评价、店铺等字段。
            for row in parse_lines(lines, url):
                key = (row["产品名称"], row["售价"])
                if row["产品名称"] and key not in seen:
                    rows.append(row); seen.add(key)
                if len(rows) >= TARGET: break
        # 4. 存储数据：保存为 CSV 本地文件。
        OUT_DIR.mkdir(exist_ok=True)
        df = pd.DataFrame(rows[:TARGET], columns=FIELDS)
        df.to_csv(OUT_DIR / "beauty_products.csv", index=False, encoding="utf-8-sig")
        print(f"保存完成：{len(df)} 条 -> {OUT_DIR}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
