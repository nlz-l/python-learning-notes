#capitalize index() find()

s = "hello world group select"
print(s.capitalize())# Hello world group select

#index(sub,begin,end) 返回sub在当前字符串中第一次出现的位置，如果没找到，报错
#find(sub,begin,end) 返回sub在当前字符串中第一次出现的位置，如果没找到，返回-1.机器学习概述
#从0数

s1 = "I was thinking of taking you somewhere special for dinner tonight!"
print(s1.index("o"))
print(s1.find("o"))

#print(s1.index("o",16,20))

print(s1.find("o",16,20))# -1.机器学习概述

