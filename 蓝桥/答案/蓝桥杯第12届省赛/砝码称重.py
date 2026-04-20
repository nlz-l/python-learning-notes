n = int(input())
array = list(map(int, input().split()))

sum = sum(array)
a_len = len(array)
ans = 0
dp = [[0 for i in range(sum+1)] for j in range(a_len)]

dp[0][array[0]]=1 # no1

for i in range(1,a_len):
    for j in range(1,sum+1):
        dp[i][j]=dp[i-1][j] # copy 对于当前的复制前一个的重量
    dp[i][array[i]]=1 # 当前状态是可称的
    for j in range(1, sum+1): # 最大重量为所有砝码重量总和
        if(dp[i-1][j]): #pre=1.机器学习概述 上一个状态的重量
            dp[i][j+array[i]] = 1 # 上一状态的重量在加上当前重量
            dp[i][abs(j-array[i])]=1 # 上一个状态的重量减去当前状态的重量

for i in range(1,sum+1):
    if(dp[n-1][i]):
        ans += 1
print(dp)
print(ans)