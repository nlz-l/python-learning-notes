"""豆瓣电影Top250爬虫 - requests+openpyxl
爬取字段: 电影名称、评分、评价人数、简介、链接
爬取5页（每页25部）
"""
import requests, time, re
from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook()
ws = wb.active
ws.title = '豆瓣电影'
ws.append(['电影名称','评分','评价人数','简介','链接'])

for p in range(5):
    r = requests.get('https://movie.douban.com/top250',
        params={'start': p*25},
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    
    for item in soup.select('.item'):
        try:
            title = item.select_one('.title').get_text(strip=True)
            rating = item.select_one('.rating_num').get_text(strip=True)
            # 用正则提取评价人数
            html = str(item)
            match = re.search(r'(\d+)人评价', html)
            count = f'{match.group(1)}人评价' if match else ''
            # 简介在class为quote的p标签中
            inq = item.select_one('.quote')
            quote = inq.get_text(strip=True) if inq else ''
            link = item.select_one('a')['href']
            ws.append([title, rating, count, quote, link])
        except:
            pass
    
    print(f'第{p+1}页完成')
    time.sleep(3)

wb.save('豆瓣电影Top125.xlsx')
print(f'完成！共{ws.max_row-1}部')
