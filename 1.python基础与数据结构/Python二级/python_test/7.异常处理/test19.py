# 异常处理
"""
1.机器学习概述.
try:
    <语句块1>
except:
    <语句块2>

2.
try:
    <语句块1>
except <异常类型>:
    <语句块2>
except:
    <语句块3>
"""

try:
    score = float(input("请输入你的成绩:"))
    print(score)
except:
    print("程序出错了，请稍侯. . .")
