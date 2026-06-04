from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周正若</nick>
        <nick class="jay">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

et = etree.XML(xml)
# result = et.xpath("/book")
# result = et.xpath("/book/name/text()")[0]
# result = et.xpath("/book//nick)")  #  // 表示所有
# result = et.xpath("/book/*/nick/text()") # * 谁都行
# result = et.xpath("/book/author/nick[@class='jay']/text()")  # 属性拿内容
# result = et.xpath("/book/partner/nick/@id") # 拿属性
# print(result)


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sogou.com">搜狗</a></li>    
    
    </ul>
    <ol>
        <li><a href="feiji">飞机</a></li>
        <li><a href="dapao">大炮</a></li>
        <li><a href="huoche">火车</a></li>
    </ol>
    
    <div class="job">李嘉诚</div>
    <div class="common">胡辣汤</div>
</body>
</html>
"""

et = etree.HTML(html)
# li_list = et.xpath("/html/body/ul/li[2]/a/text()")[0] # 不从0数
# print(li_list)

li_list = et.xpath("//li")
for li in li_list:
    href = li.xpath("./a/@href")[0]
    text = li.xpath("./a/text()")[0]
    print(text,href)