def func():
    dp = [[0 for i in range(n + 2)] for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == '(':
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j + 1]
    for i in range(n + 1): 
        if dp[n][i]:
            return dp[n][i]

s = list(input())
n = len(s)
mod = 10 ** 9 + 7
left = func()
s.reverse()
for i in range(n):
    if s[i] == ')':
        s[i] = '('
    else:
        s[i] = ')'
right = func()
print(left * right % mod)
