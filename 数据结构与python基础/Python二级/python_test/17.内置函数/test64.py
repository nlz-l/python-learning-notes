# eval(s) 计算字符串 s 作为 python 表达式的值
# exec(s) 计算字符串 s 作为 python 语句的值
# range(a,b,s) 从 a 到 b (不包含b) 以 s 为步长产生一个序列

# eval(s)

ls = "[1,2,3,56]"
ls = eval(ls)
print(ls)

score = eval(input("请输入你的成绩："))
print(score)
print(type(score))

value = 123
a = eval("value")
print(a)
print(eval("1+999"))
#exec(s)

exec("a = 1 +999")
print(a)

#range(a,b,c)
sum = 0
for i in range(1,101): #左闭右开
    sum += i
print(sum)
    
for i in range(0,101,2):
    print(i)
