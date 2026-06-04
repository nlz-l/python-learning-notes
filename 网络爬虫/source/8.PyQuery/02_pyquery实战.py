import requests
from pyquery import PyQuery

# 选第几个 div:nth-child(n)   已提取的用("div").eq().text()

def get_page_source(url,header):
    resp = requests.get(url,headers=header)
    resp.encoding = "utf-8"
    return resp.text
def parse_page_source(html):
    n = 0
    f = open("./data/懂车帝评分.csv","w",encoding="utf-8")
    doc = PyQuery(html)
    mt_list = doc(".tw-flex.tw-justify-around.tw-w-400.tw-py-12.xl\\:tw-w-auto.xl\\:tw-grid-cols-12").items()
    for mt in mt_list:
        n += 1
        l1 = mt("div > p.styles_score-item__2KcxU").text()
        l1 = list(l1.split())
        f.write(f'评分第{n}条,{l1[0]},{l1[1]},{l1[2]},{l1[3]},{l1[4]},{l1[5]},{l1[6]}\n')
        print(f"第{n}条数据保存完毕")
    f.close()
def main():
    url = "https://www.dongchedi.com/auto/series/score/20154-x-x-x-x-x"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    }
    html = get_page_source(url, header)
    parse_page_source(html)
    print("数据已保存完毕")
if __name__ == '__main__':
    main()