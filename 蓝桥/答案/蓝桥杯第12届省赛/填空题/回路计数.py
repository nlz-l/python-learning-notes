from math import gcd
n = int(input())
m = 1 << n
dp = [[0 for j in range(n)] for i in range(m)]  # dp[i][j]对于状态i，i的二进制表示中为1的位置 表示走过了教学楼j
load = [[False for j in range(n)] for i in range(n)]  # 存储i, j之间是否有路
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if gcd(i, j) == 1:
            load[i - 1][j - 1] = True
dp[1][0] = 1
for i in range(1, m):  # 枚举每一种状态
    for j in range(n):
        if i >> j & 1:  # 判断状态i是否包含第j栋教学楼
            for k in range(n):  # 枚举所有可能从教学楼k走到教学楼j的情况
                if i - (1 << j) >> k & 1 and load[k][j]:  # 判断状态i除去j后是否包含k
                    dp[i][j] += dp[i - (1 << j)][k]
print(sum(dp[m - 1]) - dp[m - 1][0])
