# -*- coding: utf-8 -*-
"""
使用 XPath 爬取数据
主题：大学生使用人工智能对学习影响
数据源：必应搜索
字段：标题、链接、摘要、来源、序号
页数：5页
"""

import requests
from lxml import etree
import json
import time
import sys

# 修复 Windows 控制台编码问题
sys.stdout.reconfigure(encoding='utf-8')

def search_bing(keyword, page):
    """必应搜索"""
    url = "https://www.bing.com/search"
    params = {
        'q': keyword,
        'first': page * 10 + 1  # 每页10条
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://www.bing.com/',
    }
    
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.encoding = 'utf-8'
    return response.text

def parse_bing(html, page_num):
    """使用 XPath 解析必应搜索结果"""
    tree = etree.HTML(html)
    
    # XPath 表达式
    items = tree.xpath('//li[@class="b_algo"]')
    
    data_list = []
    for i, item in enumerate(items):
        # 提取标题
        title = item.xpath('.//h2/a/text()')
        title = title[0].strip() if title else ""
        
        # 提取链接
        link = item.xpath('.//h2/a/@href')
        link = link[0] if link else ""
        
        # 提取摘要
        content = item.xpath('.//p/text()')
        content = content[0].strip() if content else ""
        
        # 提取来源
        source = item.xpath('.//cite/text()')
        source = source[0].strip() if source else ""
        
        if title and link:
            data_list.append({
                '序号': page_num * 10 + i + 1,
                '标题': title,
                '链接': link,
                '摘要': content[:100] + "..." if len(content) > 100 else content,
                '来源': source
            })
    
    return data_list

def main():
    keyword = "大学生使用人工智能对学习影响"
    all_data = []
    
    print(f"开始爬取：{keyword}")
    print("=" * 60)
    
    for page in range(5):
        print(f"\n正在爬取第 {page + 1} 页...")
        try:
            html = search_bing(keyword, page)
            results = parse_bing(html, page)
            all_data.extend(results)
            print(f"  获取 {len(results)} 条数据")
            time.sleep(1)  # 延时防反爬
        except Exception as e:
            print(f"  第 {page + 1} 页出错：{e}")
    
    # 保存数据
    with open('xpath_result.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'=' * 60}")
    print(f"爬取完成！共 {len(all_data)} 条数据")
    print("数据已保存到 xpath_result.json")
    
    # 显示前3条
    print(f"\n前3条数据预览：")
    for item in all_data[:3]:
        print(f"\n序号：{item['序号']}")
        print(f"标题：{item['标题']}")
        print(f"来源：{item['来源']}")

if __name__ == '__main__':
    main()
