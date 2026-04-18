# 60分
N,K=list(map(int,input().split()))
num=[]
for i in range(N):
    num.append(int(input()))
# print(num)
for i in range(N):
    for j in range(N-i-1):
        if abs(num[j])<abs(num[j+1]):
            num[j],num[j+1]=num[j+1],num[j]#交换位置
# print("排序：{}".format(num))
#统计前K个数的负数有多少个
count=0
s,s1,m=1,1,0
for i in range(K):
    if num[i]<0:
        count+=1
if count%2==0 or K==N:
    for i in range(K):
        s*=num[i]
elif count%2!=0:
    for i in range(K-1):
        s1*=num[i]
    #负数，换成正的
    if num[K-1]<0:
        while K+m<N:
            if num[K+m]>=0:
                s=s1*num[K+m]
                break
            else:
                m+=1
        else:
            # [K,N]中都为负数，说明要求最小负数
            for j in range(N-K,N):
                s*=num[j]
    else:
        while K+m<N:
            if num[K+m]<=0:
                s=s1*num[K+m]
                break
            else:
                m+=1
        #[K,N]中都为正数
        else:
            pass

if s>0:
    print(s%1000000009)
else:
    print(0-((0-s)%1000000009))
