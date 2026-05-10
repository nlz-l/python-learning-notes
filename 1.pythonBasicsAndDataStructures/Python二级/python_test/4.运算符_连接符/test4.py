#运算符
#/商
#//整除
#/%取余

x = 10
y = 4
z = 3
c = 2
print(x + y)#加
print(x - y)#减
print(x * y)#乘
print(x / y)#除
print(x // y)#整数
print(x % y)#取余数
print(x % z)#取余数
print(c ** z)#幂运算

s1 = "how"
s2 = " are you"
i =123
print(s1 +s2)
#print(s1 + i) #报错
print(s1 + str(i))

print(s1 * 4)

a = 3
b = 5
a,b = b,a
print(a,b)
a,b = b,a
print(a,b)
print("a的值为：" + str(a))
print("b的值为：" + str(b))
x = y = 123
s1 = s2 = s3 = "hello world"
print(x,y)
print(s1,s2,s3)

i = 10
i += 1#i = i+1.机器学习概述
print(i)
