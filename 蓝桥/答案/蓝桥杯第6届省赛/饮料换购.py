n=int(input())#初始多少瓶
sum=n
yu=0
while n>=3:
    a,b=n//3,n%3
    sum+=a#换购
    n=a+b
print(sum)