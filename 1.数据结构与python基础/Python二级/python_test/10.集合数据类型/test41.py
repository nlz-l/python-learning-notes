# len(x)  x in s  x not in s

s = {123,345,3.14,5.25}

print(len(s))

print(123 in s)#True

print(123 not in s)#False

# s.add() 如果数据项 x 不在集合 s 中，将 x 添加到s
s.add(124)
print(s)

# s.remove(x) 如果 x 在集合 s 中，移除该元素，不在则产生KeyError异常

s.remove(123)
print(s)
#s.remove(123) 报错

# s.clear() 移除 s 中的所有元素
s.clear()
print(s)# set()

