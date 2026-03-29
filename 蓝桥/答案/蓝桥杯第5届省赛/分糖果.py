def same(l):
    samecan=l[0]
    for c in l:
        if c!=samecan:
            return False
    return True
N=eval(input())
candy=list(map(int,input().split()))
can=[]
count=0
while True:
    #将手里的糖果分一半给左手边的小朋友
    can=[c/2 for c in candy]
    # print(can)
    for i in range(N):
        if i==N-1:
            candy[i]=candy[i]/2+can[0]
            if candy[i] % 2 !=0:
                candy[i]+=1
                count+=1
            # print(candy[i])
        else:
            candy[i]=candy[i]/2+can[i+1]
            #为奇数的孩子补发糖果
            if candy[i] % 2 !=0:
                candy[i]+=1
                count+=1
            # print(candy[i])
    if same(candy):
        print(count)
        break
