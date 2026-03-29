import math

while True:
    try:
        n = int(input())
        s = []
        g = 0
        dp = [0 for i in range(10000)]
        dp[0] = 1
        for i in range(n):
            s.append(int(input()))
            if i == 0:
                g = s[i]
            else:
                g = math.gcd(s[i], g)  # 在输入的时候求出最大公约数
            for y in range(1, len(dp)):
                if y >= s[i] and dp[y - s[i]] == 1:
                    dp[y] = 1

        if g == 1:
            print(dp.count(0))
        else:
            print('INF')
    except:
        break