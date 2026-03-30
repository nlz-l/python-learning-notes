#len(x) str(x) chr(x) ord(x) hex(x) oct(x)

#len(x) 返回字符串x的长度，也可以返回其他组合数据类型的元素个数

s = "Hello"
print(len(s))

#str(x) 返回任意类型x所对应的字符串形式

a = 123
a = str(a)
print(type(a))

#chr(x) 返回Unicode编码x对应的单个字符

print(chr(97))

#ord(x) 返回单字符x表示的Unicode编码

print(ord("a"))

#hex(x) 返回整数x对应十六进制的小写形式字符串

print(hex(10))
print(hex(22))

#oct(x) 返回整数x对应的八进制数的小写形式字符串

print(oct(10))
print(oct(40))

