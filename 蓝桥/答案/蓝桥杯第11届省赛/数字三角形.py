#动态规划-数字三角形
#从顶端开始走出一条和最大的路径，且只能往下一层最近的左边或右边走。左右走的次数相差不能超过1
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            a[i][j]+=a[i-1][j]
        elif j==i:
            a[i][j]+=a[i-1][j-1]
        else:
            a[i][j]+=max(a[i-1][j-1],a[i-1][j])#中间行返回上方相邻两个最大值
if n&1:#奇数行，返回中间值
    print(a[-1][n//2])
else: #偶数行，返回中间两个的最大值
    print(max(a[-1][n//2-1],a[-1][n//2]))#27
