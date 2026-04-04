n = int(input())
ls =[]
ls = list(map(int,input().split()))
print(ls)
for i in ls:
    count = 1
    if ls[i] == ls[i+1]:
        while ls[i] == ls[i+1]:
            i+1
            count += 1
    print(count)
