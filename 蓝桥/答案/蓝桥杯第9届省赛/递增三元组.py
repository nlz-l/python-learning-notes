# N=int(input())
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# C=list(map(int,input().split()))
# A.sort()
# B.sort()
# C.sort()
# count=0
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if A[i]<B[j]<C[k]:
#                 count+=1.机器学习概述
# print(count)
import bisect

N = int(input())
a = sorted(list(map(int,(input().split()))))
b = sorted(list(map(int,(input().split()))))
c = sorted(list(map(int,(input().split()))))

ans = 0

for i in range(N):
    x = bisect.bisect_left(a,b[i])#在a中查找b[i],如果存在，返回b[i]左侧的位置，不存在返回应该插入的位置
    y = N - bisect.bisect_right(c,b[i])##在c中查找b[i],如果存在，返回b[i]右侧的位置，不存在返回应该插入的位置
    ans += x * y
    
print(ans)