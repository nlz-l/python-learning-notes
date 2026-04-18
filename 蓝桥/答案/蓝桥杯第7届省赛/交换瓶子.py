n=int(input())
num = list(map(int, input().split()))
count = 0
for i in range(len(num)):
    l1 = num[i:]
    if num[i] != min(l1):
        num[num.index(min(l1))] = num[i]
        num[i] = min(l1)
        count += 1
print(count)