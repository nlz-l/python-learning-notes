import requests



def get_ip():
    url = ""
    resp = requests.get(url)
    ips = resp.json()
    for ip in ips["data"]["proxy_list"]:
        yield ip
def spider():
    url = "https://www.baidu.com"
    while 1:
        try:
            proxy_ip = next(gen)
            proxy = {
                "http": "http://" + proxy_ip,
                "https": "https://" + proxy_ip
            }
            resp = requests.get(url, proxies=proxy)
            resp.encoding = "utf-8"
            return resp.text
        except:
            print("报错了.")


if __name__ == "__main__":
    gen = get_ip() # 代理ip生成器
    for i in range(10):
        spider()
