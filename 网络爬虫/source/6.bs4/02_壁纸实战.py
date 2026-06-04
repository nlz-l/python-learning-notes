import requests
from bs4 import BeautifulSoup
import time

f = open("./data/壁纸.csv",mode="w",encoding="utf-8")
url = "https://wallhaven.cc/"
resp = requests.get(url)
resp.encoding = "utf-8"
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
a1_list = main_page.find_all("span", attrs={"class": "lg-thumb"})
n = 1
for a1 in a1_list:
    a = a1.find("a")
    href = a.get("href")
    resp1 = requests.get(href)
    resp1.encoding = "utf-8"
    page_A = BeautifulSoup(resp1.text, "html.parser")
    A = page_A.find("div", attrs={"class": "scrollbox"}).find("img")
    img1 = A.get("src")
    f.write(f"{img1}\n")
    with open(f"./img"
              f"/壁纸{n}.{img1[-3:]}",mode="wb") as f1:
        f1.write(requests.get(img1).content)
    print(f"第{n}张图片下载完毕")
    time.sleep(5)
    n += 1
a2_list = main_page.find_all("span", attrs={"class": "sm-thumb"})
for a2 in a2_list:
    a = a2.find("a")
    href = a.get("href")
    resp2 = requests.get(href)
    resp2.encoding = "utf-8"
    page_B = BeautifulSoup(resp2.text, "html.parser")
    B = page_B.find("div", attrs={"class": "scrollbox"}).find("img")
    img2 = B.get("src")
    f.write(f"{img2}\n")
    with open(f"./img"
              f"/壁纸{n}.{img2[-3:]}",mode="wb") as f2:
        f2.write(requests.get(img2).content)
    print(f"第{n}张图片下载完毕")
    time.sleep(5)
    n += 1
    resp.close()
f.close()