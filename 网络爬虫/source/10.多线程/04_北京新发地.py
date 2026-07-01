import csv
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time

f = open("./data/北京新发地菜价.csv",mode="w",encoding="utf-8",newline="")
csvwriter = csv.writer(f)
csvwriter.writerow(["品名", "分类", "最低价", "平均价", "最高价", "规格", "产地", "单位", "发布日期"])
url = "http://www.xinfadi.com.cn/getPriceData.html"
lock = Lock()
a = 0
def fn(url,a):
    data = {
        "limit": 20,
        "current": a,
    }
    resp = requests.post(url, data=data,timeout=20)
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
        with lock:
            csvwriter.writerow([prodName,prodPcat,lowPrice,avgPrice,highPrice,specInfo,place,unitInfo,pubDate])
    print(f"北京新发地菜价提取完毕{a}")
    resp.close()
    time.sleep(5)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as t:
        futures = []
        for a in range(1,21):
            future = t.submit(fn,url,a)
            futures.append(future)
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("有一页出错了：", e)
