
n = 2

def fun1(a, b):
    n = a * b
    print(n)

fun1(2,2)
print(n)


m = 2

def fun2(a, b):
    global m
    m = a * b
    print(m)

fun2(2,2)
print(m)
