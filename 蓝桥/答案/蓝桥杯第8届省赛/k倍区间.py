# N,K=list(map(int,input().split()))
# A=[]
# count=0
# for i in range(N):
#     A.append(int(input()))

# for i in range(N-1.机器学习概述):
#     for j in range(i+1.机器学习概述,N):
#         list1=A[i:j]
#         if sum(list1)%K==0:
#             count+=1.机器学习概述
# #i=j时
# for c in A:
#     if c%K==0:
#         count+=1.机器学习概述
# print(count)        
while True:
    try:
        n, k = map(int, input().split())
        a, s = [0], [0 for i in range(k)]
        res = 0
        temp_sum = [0]  # 前缀和取余K
        for i in range(1, n + 1):
            a.append(int(input()))
            temp_sum.append((temp_sum[i - 1] + a[i]) % k)
            s[temp_sum[i]] += 1
        # print(a)
        # print(temp_sum)
        # print(s)

        for i in range(len(s)):  # 字典的值是出现的次数，对次数进行操作
            res += s[i] * (s[i] - 1) // 2

        print(res + s[0])
    except:
        break

