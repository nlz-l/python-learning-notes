# import math
# N=int(input())
# tree=list(map(int,input().split()))
# n=int(math.log(N+1.机器学习概述,2))
# sn=[]
# deep=1.机器学习概述
# a=0
# b=1.机器学习概述
# while deep<=n:
#     sn.append(sum(tree[a:b]))
#     deep+=1.机器学习概述
#     a=b
#     b=a+pow(2,deep-1.机器学习概述)
# maxs=max(sn)
# print(sn.index(maxs)+1.机器学习概述)
    
n = eval(input())

l = list(map(int,input().split()))
l1 = []
a = 0
sum = 0
con = pow(2,a)-1
for i in range(n):
    if i > con:
        l1.append(sum)
        sum = l[i]
        a += 1
        con += pow(2,a)
        continue
    sum += l[i]

l1.append(sum)
print(l1.index(max(l1))+1)
