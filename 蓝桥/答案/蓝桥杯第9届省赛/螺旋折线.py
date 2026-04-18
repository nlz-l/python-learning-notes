x,y=list(map(int,input().split()))
if x==y and x<0 and y<0:
    x,y=x-1,y-1
#看成边长为2、4、6、8...递增的正方形
#按象限进行计算长度
n=max(abs(x),abs(y))#确定边长
#左边
if x==-n:
    dis=n+y+4*n*(n-1)#前n-1个正方形边长之和：4*n*(n-1)
#上边
elif y==n:
    dis=3*n+x+4*n*(n-1)
#右边
elif x==n:
    dis=5*n-y+4*n*(n-1)
#下边
elif y==-n:
    dis=7*n-x+4*n*(n-1)
else:
    dis=0
print(dis)
