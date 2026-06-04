import requests

url = "https://www.baidu.com"
resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)