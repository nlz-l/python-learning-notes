N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))
mean=round(sum(num)/N,2)
print(max(num))
print(min(num))
print(mean)
# print("{:.2f}".format(mean))
    
