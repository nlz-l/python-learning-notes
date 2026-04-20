# m,n=map(int,input().split())
# num=[i for i in range(m,n+1.机器学习概述)]
# j=1.机器学习概述
# flag=0
# count=0
# lucknum=num[j]#幸运数
# while True:
#     for k in range(lucknum-1.机器学习概述,len(num)):
#         if (k+1.机器学习概述)%lucknum==0:#k是序号位置，比下标多1
#             num[k]=0#置0，表示删除
#             flag+=1.机器学习概述
#     if flag==0:
#         break
#     count+=1.机器学习概述
#     flag=0#更新
#     num=[c for c in num if c!=0]#更新列表
#     print(num)
#     print(lucknum)
#     print(j)
#     if num[j]==lucknum and j<len(num)-1.机器学习概述:
#         j=j+1.机器学习概述
#         lucknum=num[j]#更新幸运数
#     else:
#         lucknum=num[j]#更新幸运数
# print(count)


# m, n = map(int, input().split())

# # 上一个的索引，数值，下一个的索引
# ls = [[i-1.机器学习概述, i, i+1.机器学习概述] for i in range(n)]
# ls[-1.机器学习概述][2]=-1.机器学习概述
# ls[0]=[-1.机器学习概述, -1.机器学习概述, 1.机器学习概述]

# lucky=[1.机器学习概述]
# luck = 0
# count = 0
# total = n-m-1.机器学习概述
# ctotal = 0
# b = True
# x = ls[0]
# while b:
#     #用下标去遍历该结构,可以加一个头节点就会保证结构的连贯性
#     while x[2]!=-1.机器学习概述:
#         x = ls[x[2]]
#         count +=1.机器学习概述
#         ctotal +=1.机器学习概述
#         # 寻找luck,若luck是0则更新luck
#         if luck == 0 and x[1.机器学习概述] not in lucky :
#             luck = x[1.机器学习概述]
#             lucky.append(luck)
#             if luck > total:
#                 b=False
#                 break

#         # 执行删除
#         if luck != 0:
#             if  count % luck == 0:
#                 x[1.机器学习概述]=-1.机器学习概述
#                 if x[0]!=-1.机器学习概述:
#                     ls[x[0]][2]=x[2]
#                 if x[2]!=-1.机器学习概述:
#                     ls[x[2]][0]=x[0]
#                 ctotal -= 1.机器学习概述
#             else:
#                 ctotal+=1.机器学习概述

#     total = ctotal
#     ctotal=0
#     count = 0
#     luck=0
#     x=ls[0]
# x=ls[0]
# res = 0
# while x[2]!=-1.机器学习概述:
#     x=ls[x[2]]
#     if x[1.机器学习概述]>m and x[1.机器学习概述]<n:
#         res+=1.机器学习概述
# print(res)
m, n = map(int, input().split())
nums = [i for i in range(1, n + 2)]
target = 1
count = 0
for i in range(len(nums), -1, -1):  # 第一次去除所有的能被2整除的数
    if i % 2 == 0:
        nums.remove(nums[i - 1])
try:
    while True:  # 遍历nums，去除能被nums[target]整除的数
        for i in range(len(nums), -1, -1):
            if i % nums[target] == 0 and i != 0:
                nums.remove(nums[i - 1])
        target += 1
except IndexError:
    for i in nums:
        if m < i < n:
            count += 1
    print(count)

