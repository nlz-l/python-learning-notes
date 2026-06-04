import requests
import re

f = open("./data/电影天堂2026必看热片.csv",mode="w",encoding="utf-8")
url = 'https://www.dytt8899.com/'
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)

obj1 = re.compile(r'2026必看热片.*?<ul>(?P<html>.*?)</ul>',re.S)
result1 = obj1.search(resp.text)
html = result1.group('html')
# print( html)

obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
result2 = obj2.finditer( html)

obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movie>.*?)<br />'
                  r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
for item in result2:
    href = item.group('href')
    # print(href)
    child_url = f"https://www.dytt8899.com{href}"
    child_resp = requests.get(child_url)
    child_resp.encoding = 'gbk'
    result3 = obj3.search(child_resp.text)
    movie = result3.group('movie')
    download = result3.group('download')
    # print(movie,download)
    f.write(f"{movie},{download}\n")
    resp.close()
f.close()
print("电影天堂2026必看热片提取完毕")