import json
import re
import time
from pathlib import Path
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUT = Path(__file__).with_name("beauty_products_demo.json")


def create_driver():
    options = Options()
    options.binary_location = EDGE
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,900")
    return webdriver.Edge(options=options)


def brand_from_name(name):
    match = re.match(r"([A-Za-z0-9\u4e00-\u9fa5]+)", name)
    return match.group(1) if match else name[:8]


def parse_products(lines, url):
    products = []
    for i, line in enumerate(lines):
        if re.search(r"(¥|￥)\s*\d+", line) and i + 1 < len(lines):
            name = lines[i + 1]
            if len(name) >= 8 and not name.startswith(("¥", "￥", "楼")):
                products.append({
                    "产品名称": name,
                    "品牌": brand_from_name(name),
                    "售价": line,
                    "来源页面": url,
                })
    return products[:20]


browser = create_driver()
try:
    # 1. 获取数据：打开商品搜索页面
    keyword = "美妆护肤"
    url = f"https://search.suning.com/{quote(keyword)}/"
    browser.get(url)
    time.sleep(6)

    # 2. 解析数据：使用 XPath 定位页面主体文本
    body_text = browser.find_element(By.XPATH, "//body").text
    lines = [line.strip() for line in body_text.splitlines() if line.strip()]

    # 3. 提取数据：把页面文本整理为字典列表
    products = parse_products(lines, url)

    # 4. 存储数据：使用 json.dump 保存到本地 JSON 文件
    with open(OUT, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=2)
    print(f"已保存 {len(products)} 条数据：{OUT}")
finally:
    browser.quit()
