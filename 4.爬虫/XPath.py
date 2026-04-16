import requests
from lxml import etree
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://home.meishichina.com/"
}

def get_html(url):
    """获取HTML"""
    resp = requests.get(url, headers=headers, timeout=15)
    resp.encoding = "utf-8"
    return resp.text

def parse_list(html):
    """解析列表页"""
    tree = etree.HTML(html)
    recipes = []
    
    for li in tree.xpath('//li[@data-id]'):
        name = li.xpath('.//h2/a/@title')
        if name:
            recipes.append({
                'name': name[0].strip(),
                'author': li.xpath('.//p[@class="subline"]/a/text()')[0].strip() if li.xpath('.//p[@class="subline"]/a/text()') else '未知',
                'ingredients': li.xpath('.//p[@class="subcontent"]/text()')[0].strip().replace('原料：', '') if li.xpath('.//p[@class="subcontent"]/text()') else '暂无',
                'link': li.xpath('.//h2/a/@href')[0] if li.xpath('.//h2/a/@href') else '',
                'steps': ''
            })
    return recipes

def parse_detail(html):
    """解析详情页提取做法"""
    tree = etree.HTML(html)
    desc = tree.xpath('//meta[@name="description"]/@content')
    if desc:
        import re
        text = desc[0]
        steps = re.split(r'(\d+\.)', text)
        result = [steps[i] + steps[i+1] for i in range(1, len(steps), 2) if i+1 < len(steps)]
        return '\n'.join(result[:15]) if result else text[:200]
    return '暂无做法'

def save_to_csv(data, filename='recipes_xpath.csv'):
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
