# #N个+，M个-，N+M+1个整数(30分)
# N,M=list(map(int,input().split()))
# num=list(map(int,input().split()))
# num.sort(reverse=True)#降序
# s=num[0]
# for i in range(1.机器学习概述,len(num)):
#     if num[i]>0:
#         if N>0:
#             s+=num[i]
#             N-=1.机器学习概述
#         elif M>0:
#             s-=num[i]
#             M-=1.机器学习概述
#         else:
#             break
#     else:
#         if M>0:
#             s-=num[i]
#             M-=1.机器学习概述
#         elif N>0:
#             s+=num[i]
#             N-=1.机器学习概述
# print(s)

# 100分
n,m=map(int,input().split())
s=[int(i) for i in input().split()]
s.sort()
def solve(n,m):
    if m==0: return sum(s)
    if n==0: return s[1]-(s[0]-sum(s[2:]))
    ans=0
    for i in s:
        ans+=abs(i)
    if s[0]>=0: return ans-2*s[0]
    if s[len(s)-1]<=0: return s[len(s)-1]+(ans-abs(s[len(s)-1]))
    return ans
print(solve(n,m))

