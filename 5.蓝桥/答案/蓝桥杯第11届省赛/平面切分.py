n=int(input())
l=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    l.append((a,b))
l=list(set(l))#去掉重合的
 
def getnode(l1,l2):
    a1,b1=l1[0],l1[1]
    a2,b2=l2[0],l2[1]
    if(a1==a2):
        return False
    else:
        x=(b2-b1)/(a1-a2)
        y=a1*x+b1
        x = round(x, 10)
        y = round(y, 10)  #这两句，表示最多取十位小数
        return (x,y)
 
 
ans=len(l)+1
for i in range(1,len(l)):
    node=[]  
    for j in range(i):    
        # print(i,j)    
        if(getnode(l[j],l[i])):
            (x,y)=getnode(l[j],l[i])
            node.append((x,y))
        else:
            continue
            # print(ans)
    node=list(set(node))
    # if(len(node)!=0):
    ans+=len(node)
print(ans)