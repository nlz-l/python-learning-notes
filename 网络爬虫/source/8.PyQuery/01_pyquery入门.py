from pyquery import PyQuery
#
# html = """
#     <li><a href="www.baidu.com">百度</a></li>
# """

# p = PyQuery(html)
# print(p)
# print((type(p)))

# li = p("li")
# print(li)
# a = p("a")
# print(a)
# print(type(a))

# a = p('li a')
# print(a)

# html = """
#     <li class="aaa"><a href="www.google.com">谷歌</a></li>
#     <li class="aaa"><a href="www.baidu.com">百度</a></li>
#     <li class="bbb" id="qq"><a href="www.qq.com">腾讯</a></li>
#     <li class="bbb"><a href="www.yuanlai.com">猿来</a></li>
# """
# p = PyQuery(html)
# a = p(".aaa a")
# print(a)

# a = p("#qq a")
# print(a)


# href = p("#qq a").attr("href")
# text = p("#qq a").text()
# print(href, text)

# todo 注意⚠️ 同时拿多个属性只能拿到一个
# href = p("li a").attr("href")
# print( href)

# 解决

# it = p("li a").items()
# for i in it:
#     href = i.attr("href")
#     text = i.text()
#     print(href, text)

# div = """
#     <div><span>我爱你</span></div>
# """
#
# p = PyQuery(div)
# html = p("span").html()
# text = p("span").text()
# print(html, text)
# html = p("div").html()
# text = p("div").text()
# print(html, text)

html = """
<HTML>
    <div class="aaa">哒哒哒</div>
    <div class="bbb">嘟嘟嘟</div>
</HTML>
"""

p = PyQuery(html)

# p("div.aaa").after("""<div calss="ccc">吼吼吼</div>""")
# p("div.aaa").append("""<span>我爱你</span>""")
# p("div.bbb").attr("class","aaa")
# p("div.bbb").attr('id',"12306")
# p("div.bbb").remove_attr("id")
# p("div.bbb").remove()
# print(p)

dic = {}
dic["jay"] = "周杰伦"
print(dic)
dic["jay"] = "呵呵哒"
print(dic)