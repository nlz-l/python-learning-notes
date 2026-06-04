import requests

# https://www.kuaidaili.com/free/intr/1/

url = "https://www.baidu.com"

proxy = {
    "http": "http://123.169.39.210:9999",
    "https": "https://123.169.39.210:9999"
}

resp = requests.get(url, proxies=proxy)
resp.encoding = "utf-8"
print(resp.text)