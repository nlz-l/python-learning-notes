import requests
f = open("./data/北京新发地菜价.csv",mode="w",encoding="utf-8")
url = "http://www.xinfadi.com.cn/getPriceData.html"
a = 0
while a <20:
    a += 1
    data = {
        "limit": 20,
        "current": a,
    }
    resp = requests.post(url,data=data)
    resp.encoding = 'utf-8'
    dict = resp.json()['list']
    for i in dict:
        prodName = i['prodName']
        prodPcat = i['prodPcat']
        lowPrice = i['lowPrice']
        avgPrice = i['avgPrice']
        highPrice = i['highPrice']
        specInfo = i['specInfo']
        place = i['place']
        unitInfo = i['unitInfo']
        pubDate = i['pubDate']
        f.write(f'{prodName},{prodPcat},{lowPrice},{avgPrice},{highPrice},{specInfo},{place},{unitInfo},{pubDate}\n')
    resp.close()
f.close()
print("北京新发地菜价提取完毕")
