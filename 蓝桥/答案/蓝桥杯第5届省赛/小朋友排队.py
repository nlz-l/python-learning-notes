n=eval(input())#小朋友个数
H=list(map(int,input().split()))#每个小朋友的身高
sum=0#不高兴程度
happy={}
for i in range(n):
    happy[H[i]]=0
for i in range(n):
    for j in range(n-i-1):
        if H[j]>H[j+1]:
            H[j],H[j+1]=H[j+1],H[j]#调换位置
            happy[H[j]]+=1
            happy[H[j+1]]+=1
        else:
            continue
#计算不高兴程度
for h in happy.values():
    sum+=int(h*(h+1)/2)