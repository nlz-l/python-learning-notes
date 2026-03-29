import fractions
#75分
# def hz(m,n):#判断互质
#     while n!=0:
#         r=m % n
#         m=n
#         n=r
#     if m==1:
#         return True
#     else:
#         return False
def printyu(yu):
    if '/' not in str(yu):
        print("{}/1".format(yu))
    else:
        print(yu)
n=int(input())
num = list(map(int, input().split()))#奖金数额
gb=[]
yu=0
#第一步：去掉重复数额
num=list(set(num))
#第二步：排序（升序）
num.sort()
n=len(num)
#第三步：获取相邻数之间的比值
for i in range(n-1):
    gb.append(num[n-i-1]/num[n-i-2])
#如果比值都相等，那么则可以判断为最大的公比
if len(set(gb))==1:
    yu=fractions.Fraction(gb[0])
    printyu(yu)
#比值不等，则去掉重复比值，并且排序。取前两个比值，进行辗转相除（必然能除尽），直到商小于最小的比值
else:
    gb=list(set(gb))#去掉重复值
    gb.sort()#排序
    b1=gb[0]
    b2=gb[1]
    yu=b2/b1
    while yu>b1:
            b2=yu
            yu=b2/b1 
    yu=fractions.Fraction(yu)
    printyu(yu)
        
