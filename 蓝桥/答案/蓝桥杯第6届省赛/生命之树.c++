#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#define INF 0x3f3f3f3f
#define mem(a,b) memset(a,b,sizeof(a))
#define For(a,b) for(int i = a;i<b;i++)
#define ll long long
#define MAX_N 100010
using namespace std;
struct ssp
{
    int u;
    int next;
}edge[MAX_N];
int x[MAX_N];
int dp[MAX_N][2],head[MAX_N];
int sum;
 
void add(int v,int u)
{
    edge[sum].u = u;
    edge[sum].next = head[v];
    head[v] = sum ++;
    //cout<<sum<<' '<<u<<' '<<edge[sum-1].next<<' '<<head[v]<<endl;
 
 
    edge[sum].u = v;
    edge[sum].next = head[u];
    head[u] = sum ++;
    //cout<<sum<<' '<<v<<' '<<edge[sum-1].next<<' '<<head[u]<<endl;
 
    return ;
}
 
void dfs(int s,int last)
{
    for(int i = head[s]; i != -1; i = edge[i].next)
    {
        int u = edge[i].u;
        if(u == last) continue;
        {
            dfs(u,s);
            dp[s][0] = max(dp[u][0],dp[u][1]);
            dp[s][1] = max(dp[s][1] + dp[u][1],dp[s][1]);
        }
    }
    return ;
}
 
int main()
{
    int n;
    cin>>n;
    mem(dp,-INF);
    mem(head,-1);
    sum = 0;
    for(int i = 1; i<=n; i++)
    {
        cin>>x[i];
        dp[i][1] = x[i];
    }
    for(int i = 0; i<n-1; i++)
    {
        int v,u;
        cin>>v>>u;
        add(v,u);
    }
    dfs(1,-1);
    int ans = max(dp[1][0],dp[1][1]);
    printf("%d\n",ans);
    return 0;
}