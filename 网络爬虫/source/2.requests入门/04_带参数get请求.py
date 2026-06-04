import requests

url = 'https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0",
}
data ={
    'limit':50
}
resp = requests.get(url,params=data,headers=headers)
# print(resp.text)
# print(resp.json())
print(resp.request.url)