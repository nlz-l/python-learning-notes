# lambda 表达式
# lambda 参数：返回值


# 传入一个参数x,返回x的平方

def fun1(x):
    return x ** 2

print(fun1(3))


#lambda

fun2 = lambda x : x ** 2
print(fun2(4))

def fun3(x,y):
    return x + y
print(fun3(1,1))

fun4 = lambda x,y : x + y
print(fun4(2,2))
