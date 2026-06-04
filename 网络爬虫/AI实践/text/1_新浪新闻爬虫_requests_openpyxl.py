import requests, time, datetime
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = '新浪新闻'
ws.append(['标题','简介','时间','详情','链接'])
for p in range(1, 6):    # 爬取5页新闻数据
    r = requests.get('https://feed.mix.sina.com.cn/api/roll/get',     # 请求新浪新闻API接口
        params={'pageid':'153','lid':'2516','num':'20','page':p})
    data = r.json()['result']['data']       
    for n in data: # 处理每条新闻数据
        ct = datetime.datetime.fromtimestamp(int(n.get('ctime','0')))  # 将Unix时间戳转换为可读时间
        ws.append([n.get('title',''), n.get('intro','')[:100], ct, '', n.get('url','')])        # 提取标题、简介(前100字符)、时间、链接，详情留空   
    print(f'第{p}页: {len(data)}条')
    time.sleep(2)  # 避免请求过快
wb.save('新浪新闻.xlsx')
print(f'完成！共{ws.max_row-1}条数据')
