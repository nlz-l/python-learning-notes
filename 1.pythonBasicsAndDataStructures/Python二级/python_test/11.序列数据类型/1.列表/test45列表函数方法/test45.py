#ls.append(x) ls.insert(i,x) ls.clear() ls.pop(i) ls.remove(x)
#ls.reverse() ls.index(x) ls.count(x) ls.copy()


ls = list() # ls = [] ls = list([])
print(ls)
print(type(ls)) #<class 'list'>
#ls.append(x) 在列表 ls 末尾处理添加一个新元素 x

ls.append(123)
ls.append("Hello")
print(ls)# [123, 'Hello']

#ls.insert(i,x) 在列表 ls 第 i 位增加元素 x
ls.insert(1,"world")
print(ls)# [123, 'world', 'Hello']


#ls.pop(i) 将列表篇 ls 中第 i个元素删除

ls.pop()# 默认删除最后一位
print(ls)# [123, 'world']
ls.pop(0)
print(ls)
ls.append(123)
ls.append("Hello")

#ls.remove(x) 将列表中出现的第一个元素 x 删除

ls.remove(123) # 没有则报错
print(ls)

#ls.reverse() 将列表 ls 中的元素反转


l2 = [123,234,3.14,65,"abc","helloWorld"]
l2.reverse()
print(l2)
l2.reverse()

#ls.index(x) 列表 ls中第一次出现元素 x 的位置

print(l2.index(123))
 

#ls.count(x) 列表 ls 中出现 x 的总次数

print(l2.count(123))



#ls.clear() 清空列表 ls 中所有元素

l2.clear()
print(l2)


#ls.copy() 返回一个新列表，复制 ls 中所有元素

a = [123,234,567]
b = a
b[1] = 3.14
print(a)
print(b)
# 上述a，b的值相等[123, 3.14, 567]
                 #[123, 3.14, 567]
a1 = [123,234,567]
b1 = a1.copy()
b1[1] = 3.14
print(a1)#[123, 234, 567]
print(b1)#[123, 3.14, 567]




