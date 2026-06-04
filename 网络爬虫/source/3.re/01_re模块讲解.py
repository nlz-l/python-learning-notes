import re

# todo 1
# result = re.findall("a","我是一个abcdefga")
# print(result)

# result = re.findall(r"\d+","我今年18岁,我有2000块")
# print(result)

# todo 2
# result = re.finditer(r"\d+","我今年18岁,我有2000块")
# #print(result)  #<callable_iterator object at 0x000001DAAF2076D0>
# for item in result:
#     # print(item) # <re.Match object; span=(3, 5), match='18'>
#                 # <re.Match object; span=(9, 13), match='2000'>
#     print(item.group())

# todo 3
# result = re.search(r"\d+","我叫周杰伦,今年32岁,我的班级是3年2班")
# # print(result)  # 只拿第一次匹配的内容  <re.Match object; span=(8, 10), match='32'>
# print(result.group())  # 32

# todo 4
# match 只匹配开头 也只找一个结果
# result = re.match(r"\d+","我叫周杰伦,今年32岁,我的班级是3年2班")
# print(result) #None

# todo 5
# 预加载
# obj = re.compile(r"\d+")
# result = obj.findall("我叫周杰伦,今年32岁,我的班级是3年2班")
# print(result)

# todo 6

s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10086'>中国移动</span></div>
"""
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
result = obj.finditer(s)
for item in result:
    id = item.group('id')
    print(id)
    name = item.group('name')
    print(name)









