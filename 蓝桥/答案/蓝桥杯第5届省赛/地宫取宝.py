n,m,k=map(int,input().split())
table=[]
for _ in range(n):
    table.append(list(map(int,input().split())))
dp=[[[[-1]*15 for _ in range(15)] for _ in range(51)]for _ in range(51)]
def dfs(x,y,sum,max):
    if dp[x][y][sum][max+1]!=-1:
        return dp[x][y][sum][max+1]
    t=0
    if x==n-1 and y==m-1:
        if table[x][y]>max:
            if sum==k or sum==k-1:
                t+=1
        elif k==sum:
            t+=1
        dp[x][y][sum][max+1]=t
        return dp[x][y][sum][max+1]
    if x+1<n:
        if table[x][y]>max:
            t+=dfs(x+1,y,sum+1,table[x][y])
            t%=1000000007
        t+=dfs(x+1,y,sum,max)
        t%=1000000007
    if y+1<m:
        if table[x][y]>max:
            t+=dfs(x,y+1,sum+1,table[x][y])
            t%=1000000007
        t+=dfs(x,y+1,sum,max)
        t%=1000000007
    dp[x][y][sum][max+1]=t
    return dp[x][y][sum][max+1]
dp[0][0][0][0]=dfs(0,0,0,-1)
print(dp[0][0][0][0])