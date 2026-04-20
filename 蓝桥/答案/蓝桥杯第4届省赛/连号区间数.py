#20分
# N=eval(input())
# num=list(map(int,input().split()))
# count=N
# for i in range(1.机器学习概述,N):#从第2个开始取
#     temp=num[0:i+1.机器学习概述]#前[1.机器学习概述,i]组成区间
#     temp.sort()
#     for j in range(1.机器学习概述,len(temp)):
#         s=temp[j]-temp[j-1.机器学习概述]
#         if s!=1.机器学习概述:
#             break
#     if j==len(temp)-1.机器学习概述:
#         count+=1.机器学习概述
# print(count)
#100分
class Solution():
    def numSection(self, n,array):
        s=0
        for left in range(n):
            min_value=max_value=array[left]            
            for right in range(left+1,n):
                max_value=max(max_value,array[right])
                min_value=min(min_value,array[right])
                flag=max_value-min_value
                if right-left==flag:
                    s+=1
                 #只要添加这么一句就行
                if flag+1>right-left+1+n-1-right:
                    break
        return s+n   

if __name__ == "__main__":
    solution = Solution
    n=int(input())
    array=[int(i) for i in input().split()]

    result = solution.numSection(solution,n,array)
    print(result)


