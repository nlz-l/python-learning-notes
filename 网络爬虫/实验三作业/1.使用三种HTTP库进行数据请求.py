import urllib.request
import urllib.parse

url = "https://httpbin.org/get"
params = {'q': '大学生 人工智能 学习'}
query_string = urllib.parse.urlencode(params)
full_url = f"{url}?{query_string}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}

req = urllib.request.Request(full_url, headers=headers)
response = urllib.request.urlopen(req, timeout=10)
html_content = response.read().decode('utf-8')
print(f"状态码: {response.status}")
print(f"内容长度: {len(html_content)} 字符\n")


import urllib3
http = urllib3.PoolManager()
response = http.request('GET', url, fields=params, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, timeout=10)
print(f"状态码: {response.status}")
html_content = response.data.decode('utf-8')
print(f"内容长度: {len(html_content)} 字符\n")
 
import requests
   
response = requests.get(url, params=params, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, timeout=10)
print(f"状态码: {response.status_code}")
print(f"编码: {response.encoding}")
html_content = response.text
print(f"内容长度: {len(html_content)} 字符\n")

from bs4 import BeautifulSoup
import json
   
soup = BeautifulSoup(html_content, 'html.parser')
   
# 查找文章列表（根据实际网站结构调整选择器）
articles = soup.find_all('div', class_='ContentItem')
   
data_list = []
for i, article in enumerate(articles[:5]):  # 取5篇文章
    # 提取标题
    title = article.find('h2').text.strip() if article.find('h2') else ""
       
    # 提取作者
    author = article.find('a', class_='UserLink-link').text.strip() if article.find('a', class_='UserLink-link') else ""
       
    # 提取时间
    time_elem = article.find('time')
    publish_time = time_elem['datetime'] if time_elem and 'datetime' in time_elem.attrs else ""
    
    # 提取点赞数
    vote_elem = article.find('button', class_='VoteButton')
    vote_count = vote_elem.text.strip() if vote_elem else "0"
    
    # 提取内容摘要
    content_elem = article.find('span', class_='RichText')
    content = content_elem.text.strip()[:100] + "..." if content_elem else ""
    
    data_list.append({
        '序号': i+1,
        '标题': title,
        '作者': author,
        '发布时间': publish_time,
        '点赞数': vote_count,
        '内容摘要': content
    })

# 保存数据
with open('bs4_data.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=2)
