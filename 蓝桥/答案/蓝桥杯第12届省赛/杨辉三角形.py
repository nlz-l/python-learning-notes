def yh(n):#杨辉三角
    # n=int(input())
    y=[[0 for j in range(i+1)] for i in range(n)]#创建二维列表
    for i in range(n):
        if i==0:
            y[i][0]=1
        elif i==1:
            y[i][0]=1
            y[i][1]=1
        else:
            for j in range(i+1):
                if j==0 or j==i:
                    y[i][j]=1
                else:
                    y[i][j]=y[i-1][j-1]+y[i-1][j]
    return y
def indexy(N):
    n=1
    while True:
        y=yh(n)
        for i in range(n):
            if N in y[i]:
                j=y[i].index(N)+1#计算N在当前行的位置
                j0=int(i*(i+1)*0.5)#计算前n行的个数
                print(j+j0)
                return
        n+=1
# test
N=eval(input())
indexy(N)
