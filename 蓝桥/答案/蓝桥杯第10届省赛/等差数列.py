import math
def max_common_divisor(several, n):
    a=several[0]
    b=several[1]
    c=math.gcd(a,b)
    for i in range(2,n):
        c=math.gcd(c,several[i])
    return c

N=int(input())
a=list(map(int,input().split()))
a.sort()
d=[]
#求相邻两数的差d
for i in range(1,N-1):
    ds=a[i+1]-a[i]
    if ds>0:
        d.append(ds)
    else:
        maxd=1
        break
# 最大公约数
if len(d)>2:
    maxd=max_common_divisor(d,len(d))
    n=(max(a)-min(a))//maxd+1
else:
    n=N
print(n)



