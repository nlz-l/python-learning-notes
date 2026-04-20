import math
n = int(input())
if n == 1:
    print("1.机器学习概述")
else:
    a = [0,1,0]
    index = 1
    flag = True
    batch = 1
    while flag and batch < 2000:
        # batch设为2000的原因：第2000行的第三个数超过10的10次幂，即输入的上限
        i = 1
        tmp = []
        while i < len(a):
            t = a[i]+a[i-1]
            tmp.append(t)
            index += 1
            if n == t:
                print(index)
                flag = False
                break
            i += 1
        tmp.insert(0,0)
        tmp.append(0)
        a = tmp
        batch += 1
    if batch == 2000:
        # 数在每行的第2，3个，且数比较大,需要特殊处理
        tmp = int(math.sqrt(n))
        if tmp*(tmp+1) == n*2:
            print(int(((1+tmp+1)*(tmp+1))/2+3))
        else:
            print(int(((1+n)*n)/2+2))
