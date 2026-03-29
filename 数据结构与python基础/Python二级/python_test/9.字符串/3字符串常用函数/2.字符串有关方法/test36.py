#字符串常用方法
#str.lower() str.upper() str.split(sep=None) str.count(sub)
#str.replace(old,new) str.center(width,fillchar) str.strip() str.join(iter)

#str.lower() 返回字符串str的副本，全部字符小写

s1 = "HOW ARE YOU DOING?"
s2 = "how are you doing?"
print(s1.lower())
print(s1)#不改变原字符串

#str.lower() 返回字符串str的副本，全部字符大写

print(s2.upper())
print(s2)#不改变原字符串

#str.split(sep=None) 返回一个列表，由str根据sep被分割的部分构成，
#省略sep默认以空格分隔

s3 = "asd-f-ew-we-d-23-sf"
a = s3.split("-")#不改变原字符串
print(a)#a = ['asd', 'f', 'ew', 'we', 'd', '23', 'sf'] 列表

#str.count(sub) 返回sub字符出现的次数

s4 = "abc234we32abcefwweabc34abc"
print(s4.count("abc"))


#str.replace(old,new) 返回字符串str的副本，所有old子串被替换为new

s5 = "HelloWorld"
s6 = s5.replace("o","O")#不改变原字符串
print(s6)
#str.center(width,fillchar) 字符串居中函数，fillchar参数可选

s7 = "hello"
print(s7.center(10,"="))
print(s7.center(10))# 默认空格
print(s7.center(2,"="))# 小于时直接返回

#str.strip() 从字符串str中去掉在其左侧和右侧chars中列出的字符

s8 = "  python  "
print(s8.strip())# 默认去掉空格

s9 = "=python=  "
print(s9.strip("="))#只能从两边识别

s10 = "=python=="
print(s10.strip("="))

#str.join(iter) 将iter变量的每个元素后增加一个str字符串

print(",".join("python"))# p,y,t,h,o,n
print(" ".join("python"))# p y t h o n
