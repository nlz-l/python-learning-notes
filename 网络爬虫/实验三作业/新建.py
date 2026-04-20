#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""美食天下爬虫 - 精简版"""
import requests, os, re
from bs4 import BeautifulSoup
import json, csv, time

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}


def get(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.encoding = 'utf-8'
        return r.text
    except:
        return None


def parse_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.select('a[href*="/recipe-"]'):
        href = a.get('href', '')
        if href and '/recipe-' in href and '/type' not in href and '/menu' not in href:
            if 'home.meishichina.com/recipe-' in href and href not in links:
                links.append(href)
    return list(set(links))


def parse_detail(html, url):
    soup = BeautifulSoup(html, 'html.parser')

    # 菜名
    title = soup.select_one('#recipe_title')
    title = title.get('title', title.get_text(strip=True)) if title else '未知'

    # 作者
    author = soup.select_one('#recipe_username')
    author = author.get_text(strip=True) if author else '未知'

    # 配料
    ingredients = []
    for li in soup.select('.recipeCategory_sub_R li'):
        spans = li.select('span')
        if len(spans) >= 2:
            name = spans[0].get_text(strip=True)
            amount = spans[1].get_text(strip=True)
            if name and name != '口味' and name != '工艺' and name != '耗时' and name != '难度':
                ingredients.append(f"{name}{amount}")

    # 做法
    steps = []
    for step in soup.select('.recipeStep li'):
        text = step.get_text(strip=True)
        if text:
            steps.append(text)

    return {
        '菜名': title,
        '作者': author,
        '配料': '|'.join(ingredients[:10]) if ingredients else '未知',
        '链接': url,
        '做法': ' '.join(steps[:10]) if steps else '未知'
    }


def crawl():
    all_recipes = []
    base = 'https://home.meishichina.com'

    for page in range(1, 11):
        print(f"爬取第 {page} 页...")
        html = get(f'{base}/recipe-list.html?page={page}')
        if not html: continue

        links = parse_list(html)[:5]
        print(f"  找到 {len(links)} 个")

        for link in links:
            if not link.startswith('http'):
                link = base + link
            time.sleep(1)
            detail = get(link)
            if detail:
                r = parse_detail(detail, link)
                all_recipes.append(r)
                print(f"  ✓ {r['菜名'][:15]} | {r['作者']}")
        time.sleep(2)
    return all_recipes


def save(data):
    if not data: return
    json_path = os.path.join(OUT_DIR, 'recipes.json')
    csv_path = os.path.join(OUT_DIR, 'recipes.csv')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=data[0].keys())
        w.writeheader()
        w.writerows(data)
    print(f"\n完成! 共 {len(data)} 条")
    print(f"文件: recipes.json, recipes.csv")


if __name__ == '__main__':
    save(crawl())
