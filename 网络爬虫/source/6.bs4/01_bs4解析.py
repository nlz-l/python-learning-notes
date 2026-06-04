from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="zhangwuji.com">张无忌</a></li>
    <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
    <li><a href="zhubajie.com">猪八戒</a></li>
    <li><a href="wuzetian.com">武则天</a></li>
    <a href="jinmaoshiwang.com">金毛狮王</a>
</ul>
"""

page = BeautifulSoup(html, 'html.parser')
li = page.find("li",attrs={"id":"abc"}) # 只找一个
# print(li)

# a = li.find("a")
# print(a.text)
# print(a.get("href"))


li_list = page.find_all("li") #查找所有
for li in li_list:
    a = li.find("a")
    print(a.text)
    print(a.get("href"))