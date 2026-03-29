import math

def gcm(x, y: int) -> int:  # 求最小公倍数
    return x * y // math.gcd(x, y)  # gcd求最大公约数

n = int(input())

dp = [float('inf')] * (n + 1)
dp[1] = 0
for i in range(1, n + 1):
    for j in range(i + 1, i + 22):
        if j > n:
            break
        dp[j] = min(dp[j], dp[i] + gcm(i, j))
print(dp[n])#10266837
