#数据类型

#基本数据类型
#1.数值类型
'''    引导符号
十进制     无    1100，-1100
二进制 0b或0B    0b1010,0B1010
八进制 0o或0O    0o1010,0O1010
十六进制 0x或0X  由字符0到9，a到f或A到F组成,例:0x1010,0X1010
'''
print(123)#十进制
print(0b1010)#二进制
print(0o167)#八进制
print(0x24B)#十六进制

#2.浮点类型

f1 = 1.23 #将浮点数1.23赋值给f1
f2 = 1.01e4 
print(f1)
print(f2)

#3.复数类型

#例:a+bj    当b=1时，1不能省略,即1j

print(11.3 + 4j)
num = 5 + 2j
print(num)

print(num.real)#获取变量num实部  输出浮点数
print(num.imag)#获取变量num虚部  输出浮点数

#4.字符串类型
print("Hello World")
print("Hello Kitty")
s1 = """Hello大家好，
    这里可以换行"""
print(s1)
s2 = '''Hello大家好，
    这里可以换行'''
print(s2)

#5.布尔类型
#True False
print(True)
print(False)
