# def rise(list):#冒泡排序升序
#     n=len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list
# def drop(list):#冒泡排序降序
#     n=len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j]<list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list

n,m=map(int,input().split())
num=[int(i) for i in range(1,n+1)]
op=[]
for i in range(m):
    op.append(input().split())#[[0,3],[1,2],[0,2]]
for i in op:
    j=int(i[1])
    temp=[]
    if i[0]=='0': #降序num[0]:num[i[1]]
        temp=num[0:j]
        temp.sort(reverse=True)
        # temp=drop(temp)
        if j<n:
            num=temp+num[j:]
        else:
            num=temp
    else:
        temp=num[(j-1):]
        temp.sort()
        # temp=rise(temp)
        num=num[0:j-1]+temp
for i in range(n):
    print(num[i],end=' ')

