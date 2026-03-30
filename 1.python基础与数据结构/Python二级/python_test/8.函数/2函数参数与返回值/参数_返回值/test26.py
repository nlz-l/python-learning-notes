# 输出1-100之间的和
# 1.无参数 无返回值
def fun1():
    sum = 0
    i = 1
    while i <=100:
        sum +=i
        i += 1
    print(sum)

#计算1-100之间的和，并返回
#2.无参数，有返回值
def fun2():
    sum = 0
    i = 1
    while i <=100:
        sum +=i
        i += 1
    return sum

#传入一个成绩，判断该成绩是否及格，并输出“及格”或“不及格”
#3.有参数，无返回值
def fun3(s):
    if s >=60:
        print("及格")
    else:
        print("不及格")
#实现传入一个成绩，判断该成绩是否及格，如果及格返回True，否则返回False
#3.有参数，有返回值
def fun4(s):
    if s >=60:
        return True
    else:
        return False

fun1()
print(fun2())
fun3(60)
print(fun4(59))
