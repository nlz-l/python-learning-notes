n=int(input())
cnt=0
ans=[]
#为了减少运算，需要记录所有能把n整除的整数
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        ans.append(i)
        ans.append(n//i)
case=set()
for i in ans:
    for j in ans:
        for k in ans:
            if i*j*k==n:
                # print(i,j,k)
                case.add((i,j,k))
print(len(case))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         for k in range(1,n+1):
#             if i*j*k==n:
#                 # print(i,j,k)
#                 cnt+=1
# print(cnt)
