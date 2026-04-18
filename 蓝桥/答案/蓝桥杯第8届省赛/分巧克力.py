N,K=list(map(int,input().split()))#N:巧克力块数；K：小朋友个数
qiao=[0 for _ in range(N)]
for i in range(N):
    qiao[i]=[int(c) for c in input().split()]#存入每块巧克力的长宽
def count(l):#判断该边长能否切割k块
    cnt=0
    for i in range(len(qiao)):
        cnt+=(qiao[i][0]//l)*(qiao[i][1]//l)#每块切割的个数
    if cnt>=K:
        return True
    else:
        return False
#二分法，确定边长
def length(left,right):
    while left<=right:
        mid=(left+right)//2
        if not count(mid):
            right=mid-1
        else:
            left=mid+1
    return left-1

print(length(0,100000))
# N,K = list(map(int,input().split()))
# H = []
# W = []
# for i in range(N):
#     h,w = list(map(int,input().split()))
#     H.append(h)
#     W.append(w)
# l = 0
# r = 100000
# while l <= r:
#     cnt = 0
#     mid = (l+r)//2
#     for j in range(N):
#         cnt += (H[j]//mid)*(W[j]//mid)
    
#     if cnt >= K:#切割的个数多于K，说明边长小了，可试着增大
#         l = mid + 1
#         ans = mid
#     else:
#         r = mid - 1

# print(ans)







