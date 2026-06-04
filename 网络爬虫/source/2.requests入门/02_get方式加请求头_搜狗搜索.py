import requests

context = input('请输入你要检索的内容:')
url = f"https://www.sogou.com/web?query={context}"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
}
resp = requests.get(url,headers= headers)
print(resp.text)
# print(resp.requests.headers)