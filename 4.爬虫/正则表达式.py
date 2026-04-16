# -*- coding: utf-8 -*-
"""
美食天下爬虫 - 精简版
网址: https://home.meishichina.com/recipe-list.html
爬取字段: 菜名、作者、配料、链接、具体做法
翻页: 10页
技术: requests + 正则表达式 + CSV
"""

import requests
import re
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://home.meishichina.com/"
}

# 正则表达式
recipe_pat = re.compile(r'<li data-id="\d+">(.*?)</li>', re.DOTALL)
name_pat = re.compile(r'<h2><a[^>]*title="([^"]+)"')
author_pat = re.compile(r'<p class="subline"><a[^>]*>([^<]+)</a>')
ing_pat = re.compile(r'<p class="subcontent">原料：([^<]+)</p>')
link_pat = re.compile(r'href="(https://home\.meishichina\.com/recipe-\d+\.html)"')
desc_pat = re.compile(r'<meta[^>]*name="description"[^>]*content="([^"]+)"')

def get_html(url):
    """获取HTML"""
    resp = requests.get(url, headers=headers, timeout=15)
    resp.encoding = "utf-8"
    return resp.text

def parse_list(html):
    """解析列表页"""
    recipes = []
    for item in recipe_pat.findall(html):
        name = name_pat.search(item)
        if name:
            recipes.append({
                'name': name.group(1).strip(),
                'author': author_pat.search(item).group(1).strip() if author_pat.search(item) else '未知',
                'ingredients': ing_pat.search(item).group(1).strip() if ing_pat.search(item) else '暂无',
                'link': link_pat.search(item).group(1) if link_pat.search(item) else '',
                'steps': ''
            })
    return recipes

def parse_detail(html):
    """解析详情页提取做法"""
    desc = desc_pat.search(html)
    if desc:
        steps = re.split(r'(\d+\.)', desc.group(1))
        result = [steps[i] + steps[i+1] for i in range(1, len(steps), 2) if i+1 < len(steps)]
        return '\n'.join(result[:15]) if result else desc.group(1)[:200]
    return '暂无做法'

def save_to_csv(data, filename='recipes.csv'):
    """保存数据到CSV"""
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'author', 'ingredients', 'steps', 'link'])
        writer.writeheader()
        writer.writerows(data)
    print(f"\n✅ 数据已保存到 {filename}")

# 主程序
result = []
print("开始爬取美食天下...")

for page in range(1, 11):
    url = f"https://home.meishichina.com/recipe-list{'-page-' + str(page) if page > 1 else ''}.html"
    print(f"\n正在爬第 {page} 页...")
    try:
        recipes = parse_list(get_html(url))
        print(f"  找到 {len(recipes)} 个菜谱")
        
        for i, r in enumerate(recipes[:5]):
            if r['link']:
                print(f"    获取详情: {r['name'][:15]}...")
                r['steps'] = parse_detail(get_html(r['link']))
                time.sleep(0.5)
        
        result.extend(recipes)
        time.sleep(1)
    except Exception as e:
        print(f"第{page}页出错: {e}")

print(f"\n✅ 爬取完成！共 {len(result)} 条菜谱")

# 保存CSV
save_to_csv(result)

# 显示前5条
for i, item in enumerate(result[:5], 1):
    print(f"\n--- {i} ---")
    print(f"菜名：{item['name']}")
    print(f"作者：{item['author']}")
    print(f"配料：{item['ingredients']}")
    print(f"链接：{item['link']}")
