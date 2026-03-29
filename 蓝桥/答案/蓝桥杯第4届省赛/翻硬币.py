start=list(input())#初始状态
end=list(input())#目标状态
num=0
for i in range(len(end)-1):
    if start[i]==end[i]:
        continue
    else:
        if start[i+1]=='*':
            start[i],start[i+1]=end[i],'o'
        else:
            start[i],start[i+1]=end[i],'*'
        num+=1
print(num)
