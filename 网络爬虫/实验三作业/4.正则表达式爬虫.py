import requests
import re
import json
import time
import sys

# 修复 Windows 控制台编码问题
sys.stdout.reconfigure(encoding='utf-8')

def search_360(keyword, page):
    """360搜索"""
    url = "https://www.so.com/s"
    params = {
        'q': keyword,
        'pn': page  # 页码从0开始
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://www.so.com/',
    }
    
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.encoding = 'utf-8'
    return response.text

def parse_360(html, page_num):
    """使用正则表达式解析360搜索结果"""
    data_list = []
    
    # 正则表达式
    # 匹配每个搜索结果项
    item_pattern = re.compile(r'<li class="res-list".*?</li>', re.DOTALL)
    items = item_pattern.findall(html)
    
    for i, item in enumerate(items):
        # 提取标题
        title_match = re.search(r'<h3.*?<a[^>]*>(.*?)</a>', item, re.DOTALL)
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip() if title_match else ""
        
        # 提取链接
        link_match = re.search(r'<h3.*?<a[^>]*href="([^"]+)"', item)
        link = link_match.group(1) if link_match else ""
        
        # 提取摘要
        content_match = re.search(r'<p class="res-desc">(.*?)</p>', item, re.DOTALL)
        content = re.sub(r'<[^>]+>', '', content_match.group(1)).strip() if content_match else ""
        
        # 提取来源
        source_match = re.search(r'<span class="res-tag">(.*?)</span>', item)
        source = re.sub(r'<[^>]+>', '', source_match.group(1)).strip() if source_match else ""
        
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
            html = search_360(keyword, page)
            results = parse_360(html, page)
            all_data.extend(results)
            print(f"  获取 {len(results)} 条数据")
            time.sleep(1)  # 延时防反爬
        except Exception as e:
            print(f"  第 {page + 1} 页出错：{e}")
    
    # 保存数据
    with open('regex_result.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'=' * 60}")
    print(f"爬取完成！共 {len(all_data)} 条数据")
    print("数据已保存到 regex_result.json")
    
    # 显示前3条
    print(f"\n前3条数据预览：")
    for item in all_data[:3]:
        print(f"\n序号：{item['序号']}")
        print(f"标题：{item['标题']}")
        print(f"来源：{item['来源']}")

if __name__ == '__main__':
    main()
