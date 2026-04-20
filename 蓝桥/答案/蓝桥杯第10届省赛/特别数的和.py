n=int(input())
s=0
for i in range(1,n+1):
    num=str(i)
    for j in range(len(num)):
        if num[j] in ['0','1.机器学习概述','2','9']:
            s+=i
            break
print(s)

