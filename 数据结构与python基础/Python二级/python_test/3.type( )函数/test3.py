#type()函数
'''
整数:<class'int'>
浮点数:<class'float'>
复数:<class'complex'>
字符串:<class'str'>
布尔类型:<class'bool'>
'''
a = 123
type(a)
b = 3.14
c = 5 +2j
d = "大家好"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

age = "16"
print(type(age))
age_new = int(age) #将变量age转换为整数类型并赋值给变量
print(type(age_new))

f = 5.6
aa = int(f)#将浮点类型的变量f转换为整数类型并赋值给变量aa
print(aa)#直接砍掉小数部分，只保留整数部分
print(type(aa))

#浮点数只有十进制









