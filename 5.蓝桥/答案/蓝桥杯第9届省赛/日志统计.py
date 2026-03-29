#62分
# N,D,K=list(map(int,input().split()))
# td=[0 for _ in range(N)]#存入每条日志的时间和id
# ts=[] #存入所有日志时间
# ids={}#存入用户点赞次数
# hot=[]#热帖id
# tid=[]#辅助列表
# for i in range(N):
#     td[i]=list(map(int,input().split()))
#     ts.append(td[i][0])#单独存入时间
#     tid.append(td[i][1])
# ts=list(set(ts))#去掉重复时间
# ts.sort()
# #利用字典记录不同用户id的点赞数
# ids=dict(zip(list(set(tid)),[0 for _ in range(N)]))
# for t in ts:
#     for i in range(N):
#         if td[i][1] in ids:
#             if t<=td[i][0]<t+D:
#                 ids[td[i][1]]+=1
#             if ids[td[i][1]]>=K:
#                 hot.append(td[i][1])
#                 del ids[td[i][1]]
#         else:
#             continue
#     #每遍历一遍都要清0
#     ids=dict(zip(list(set(tid)),[0 for _ in range(N)]))
# hot=list(set(hot))#去重
# hot.sort()
# for id in hot:
#     print(id)
# 100分
N, D, K = list(map(int, input().split()))
li1 = list()
li2 = dict()
flags = 0
for i in range(N):
    li1.append(tuple(map(int, input().split())))
li1.sort()
j = i = 0
count = set()
while i < N:
    # j的变化：也就是要 加上属于这个时间段的 赞
    while j < N and abs(li1[i][0] - li1[j][0]) < D:
        if li1[j][1] in li2.keys():
            li2[li1[j][1]] += 1 # 日志记录id为j的帖子加1
        else:
            li2[li1[j][1]] = 1 # 赋初值

        if li2[li1[j][1]] >= K: # 判断是不是热帖
            count.add(li1[j][1])
        j += 1
    if j>=N:
        break
    # i的变化：也就是要 减去不属于这个时间段的 赞
    while i < j and abs(li1[i][0] - li1[j][0]) >= D:
        li2[li1[i][1]] -= 1
        i += 1
qw=list(count)
qw.sort()
for i in qw:
    print(i)





