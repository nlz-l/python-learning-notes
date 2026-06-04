import requests
import re

f = open("./data/top250.csv",mode="w",encoding="utf-8")
a = 1
while a<11:
    # 1.请求
    url = f"https://movie.douban.com/top250?start={(a-1)*25}&filter="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0",
    }
    resp = requests.get(url, headers=headers)
    # resp.encoding("utf-8")
    pageSource = resp.text
    print(pageSource)

    # 2.解析
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p>.*?导演: (?P<daoyan>.*?)&nbsp;'
                     r'.*?<br>(?P<year>.*?)&nbsp'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(pageSource)
    for item in result:
        name = item.group("name")
        daoyan = item.group("daoyan")
        year = item.group("year").strip()
        score = item.group("score")
        num = item.group("num")
        f.write(f"{name},{daoyan},{year},{score},{num}\n")
    a += 1
    resp.close()
f.close()
print("豆瓣TOP250提取完毕")