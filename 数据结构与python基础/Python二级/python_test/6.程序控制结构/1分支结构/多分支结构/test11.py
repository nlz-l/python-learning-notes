#多分支结构

'''
if <条件1>:
    <语句块1>
elif <条件2>:
    <语句块2>
...
else:
    <语句块N>
'''

#输入一个成绩，判断这个成绩是及格？优秀？不及格？

score = float(input("请输入你的成绩："))

if score >=80:
    print("成绩优秀")
elif score >= 60 :
    print("普通及格")
else:
    print("不及格")
