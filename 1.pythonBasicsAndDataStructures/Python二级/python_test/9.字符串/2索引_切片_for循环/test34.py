# for遍历循环
"""
for <循环变量> in <可迭代对象>:
    <循环体>
"""

s = "How are you doing?"
for i in s:
    print(i)

for a in "HelloWorld":# w 和 W
    if a == 'w':
        continue
    print(a,end = "")

for a in "HelloWorld":
    if a == 'W':
        continue
    print(a,end = "")
