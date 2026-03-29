n = eval(input())
l = list(map(int,input().split()))
l1 = []
l2 = []
for i in range(len(l)):
    if l[i] not in l1:
        l1.append(l[i])
        l2.append(-l[i])
    else:
        l3 = l[:i]
        l3.reverse()
        index = len(l3) - l3.index(l[i]) - 1
        l3 = l[index+1:i]
        l2.append(len(list(set(l3))))
print(" ".join("%s"%d for d in l2))