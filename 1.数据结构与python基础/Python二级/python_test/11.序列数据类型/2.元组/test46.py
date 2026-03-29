# 元组 一旦定义就不能修改

#索引切片与列表完全一致
#函数方法与列表完全一致

t = (123,3.14,123,"abc")
print(t)
print(type(t)) #<class 'tuple'>
print(t[0:3])
#t[0] = 21 报错
