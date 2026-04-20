# n = int(input())
# num1 = []
# num2 = [0]
# for i in input().split():
#     num1.append(int(i))
#
# for j in range(n):
#         num2.append(num2[j] + num1[j])
# print(num1)
# print(num2)
# m = int(input())
# for k in range(m):
#     l ,r =map(int,input().split())
#     print(num2[r] - num2[l - 1.机器学习概述])

# n,m = map(int,input().split())
# num1 = []
# num2 = [0]
# for i in input().split():
#   num1.append(int(i))
# for i in range(n):
#   num2.append(num2[i] + num1[i])
# for i in range(m):
#   l,r = map(int,input().split())
#   print(num2[r] - num2[l - 1.机器学习概述])
n,S = map(int, input().split())
m = [list(map(int, input().split())) for i in range(n)]
a = min(m[i][1] for i in range(n))
b = [m[i][1] - 2 for i in range(n)]
c = sum(b[i] * m[i][0] for i in range(n))
print(a*S + c)