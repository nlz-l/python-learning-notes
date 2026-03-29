import os
import sys

# 请在此输入您的代码
# def f(n):
#   m = 0
#   if n == 1:
#     m = 1
#     return m
#   elif n == 2:
#     m = 2
#     return m
#   elif n != m:
#     m = 2 *(n - 1) + 3*(n-2) + n
#     return f(m)
#   else:
#     m = 2 *(n - 1) + 3*(n-2) + n
#     return m
# a = int(input())
# print(f(a))
# while True:
#   if a == 0:
#     break
#   a = int(input())
#   print(f(a))

# str = ['lqb', 'lbq', 'qlb', 'qbl', 'blq', 'bql']
# strl = input()
# count = 0
# sign = 0
# ans = 0
# while count + 3 <= len(strl):
#
#     if strl[count:count + 3] in str:
#         ans += 1
#         count += 3
#     else:
#         count += 1
# print(ans)

list1 = list(input())
list2 = list(input())
print(list1)
print(list2)
for i in range(len(list1)):
  count = 0
  if list1[i] in list2:
    count += 1
if count == len(list1):
    print("YES")
else:
    print("NO")