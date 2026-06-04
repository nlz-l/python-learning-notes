from urllib.request import urlopen

url = "https://www.baidu.com"
html = urlopen(url)
# print(html.read().decode('utf-8'))
with open ('./html/1_baidu.html','w',encoding='utf-8') as f:
    f.write(html.read().decode('utf-8'))