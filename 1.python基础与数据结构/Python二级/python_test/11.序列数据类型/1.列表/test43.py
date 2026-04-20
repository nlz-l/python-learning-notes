#列表 有序 可重复

ls = [123,123,3.14,"abc","abc"]
print(ls)
print(type(ls)) #<class 'list'>

#列表索引 0 - n-1.机器学习概述

print(ls[0:1])
print(ls[::-1])
print(ls[1:3])

#列表切片 同上



#多重列表
l2 = [123,234,[12,1,45],[14,16]]
print(l2)
print(l2[2])
print(l2[2][2])#45
print(l2[3][1])#16
