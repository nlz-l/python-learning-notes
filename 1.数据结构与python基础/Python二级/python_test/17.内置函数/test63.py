# abs(x) x 的绝对值。如果 x 是复数，返回复数的模
# divmod(a,b) 返回 a 和 b 的商及余数。如divmod(10,3)结果是一个(3,1)
# pow(x,y) 返回 x 的 y 次幂。如 pow(2,pow(2,2))的结果是 16
#round(n,d) 四舍五入方式计算 n  d为小数点后保留位数。如round(10.6)的结果是 11



a =-1
b = 2 + 5j
print(abs(a))
print(abs(b))#根号29

c = 5
d = 3
print(divmod(c,d))
print(type(divmod(c,d)))# <class 'tuple'>

print(pow(2,3))

print(round(5.23623,2))


#all(x) 组合类型变量 x 中所有元素都为真时返回 True, 否则返回 False;
#若 x为空，返回 True
#any(x) 组合变量 x 中任一元素都为真时返回 Ture，否则返回 False;
#若 x 为空,返回 True
#reversed(r) 返回组合类型 r 的逆序形式。
#sorted(x) 对组合数据类型 x 进行排序,默认从小到大。
#sum(x) 对组合数据类型 x 计算求和结果。


ls = [True,True,1]
print(all(ls))
l2 = [True,False,False,0]
print(any(l2))
l3 = []
print(all(l3))
print(any(l3))

l4 = [1,23,54,2,43,65]
print(list(reversed(l4)))

print(sorted(l4))

print(sum(l4))


