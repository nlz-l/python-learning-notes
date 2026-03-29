import sys
sys.setrecursionlimit(100000)  #限制递归次数
n=int(input())
li=[[] for i in range(n+1)]    #li[i]是结点i的所有子节点
# li[i]=i的子节点数量+子树转为二叉树后的最大高度
for i in range(n-1):
    temp=int(input())
    li[temp].append(i+2)
def dptest(x):
    ans=0
    for i in li[x]:
        ans=max(ans,len(li[x])+dptest(i))
    return ans

result=dptest(1)
print(result)
