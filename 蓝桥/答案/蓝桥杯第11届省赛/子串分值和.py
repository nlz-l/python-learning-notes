# 40分
# def different(s):
#     s=list(set(s))
#     return len(s)
# s=input()
# l=len(s)
# sum=0
# for i in range(l):
#     for j in range(i+1,l+1):
#         temp=s[i:j]
#         c=different(temp)
#         sum+=c
# print(sum)
# 100分
list1=list(input())
list2=[-1 for i in range(26)]
count=0

for i in range(len(list1)):
    index=ord(list1[i])-ord('a')
    count+=(len(list1)-i)*(i-list2[index])
    list2[index]=i

print(count)



