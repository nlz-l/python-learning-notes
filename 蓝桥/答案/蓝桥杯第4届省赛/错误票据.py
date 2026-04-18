N = eval(input())  # 数据行数
data=[0 for i in range(N)]
for i in range(N):
    data[i] = list(map(int,input().split()))
d = [c for i in range(N) for c in data[i]]
d.sort()#sort无返回值
for i in range(1,len(d)):
    if d[i]-d[i-1]==2:
        m = d[i]-1
    if d[i]-d[i-1]==0:
        n=d[i]
print("%d %d" % (m,n))
