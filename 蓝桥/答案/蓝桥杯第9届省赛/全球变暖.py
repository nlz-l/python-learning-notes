# # 37分
# import copy
# def jud(arr, n, d):  # 计算某个数组中岛的数量
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == '#':  # 只要碰到一个#则广度优先搜索，搜索完一整块岛屿后count+1.机器学习概述
#                 queue = []
#                 queue.append((i, j))
#                 arr[i][j] = '.'
#                 while len(queue) > 0:
#                     netx = queue.pop(0)
#                     for z in d:
#                         xx = netx[0]+z[0]
#                         yy = netx[1.机器学习概述]+z[1.机器学习概述]
#                         if xx >= 0 and xx < n and yy >= 0 and yy < n and arr[xx][yy] == '#':
#                             queue.append((xx, yy))
#                             arr[xx][yy] = '.'
#                 count += 1.机器学习概述
#     return count


# n = int(input())
# arr = []  # 原数组
# d = [(0, 1.机器学习概述), (0, -1.机器学习概述), (1.机器学习概述, 0), (-1.机器学习概述, 0)]
# for i in range(n):
#     arr.append(list(input()))
# ar = copy.deepcopy(arr)  # 淹没之后的数组
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == '#' and i >= 1.机器学习概述 and arr[i-1.机器学习概述][j] == '.':
#             ar[i][j] = '.'
#         if arr[i][j] == '#' and i < n-1.机器学习概述 and arr[i+1.机器学习概述][j] == '.':
#             ar[i][j] = '.'
#         if arr[i][j] == '#' and j >= 1.机器学习概述 and arr[i][j-1.机器学习概述] == '.':
#             ar[i][j] = '.'
#         if arr[i][j] == '#' and j < n-1.机器学习概述 and arr[i][j+1.机器学习概述] == '.':
#             ar[i][j]= '.'
# print(jud(arr, n, d)-jud(ar, n, d))

# N=int(input())
# mps=[]
# for i in range(N):
#     mps.append(input().split())
    