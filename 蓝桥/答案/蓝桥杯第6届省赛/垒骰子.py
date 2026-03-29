n,m = map(int,input().split())
list1 = [[False for _ in range(7)] for _ in range(7)]
dict1 = {1:4,2:5,3:6,4:1,5:2,6:3} # 对立面
for _ in range(m): # 不能紧贴的面
    x,y = map(int,input().split())
    list1[x][y] = True
    list1[y][x] = True         #输入不能紧贴的面 用true记录
 
mod = 10**9 + 7
ans = 0
def f(up,cnt):
    ans = 0
    if cnt==0:
        return 4  #确定up面后可以旋转
    for upp in range(1,7):
        if list1[dict1[up]][upp]:
            continue
        ans += f(upp,cnt-1)
    return ans
 
    
for up in range(1,7):
    ans += 4*f(up,n-1)
print(ans%mod)