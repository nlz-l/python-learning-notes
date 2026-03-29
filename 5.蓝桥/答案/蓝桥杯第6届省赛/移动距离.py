def rc(w,num):
    if num%w==0:
        return num//w-1,w-1
    rol=num//w
    if rol%2==0:
        return rol,num%w-1
    else:
        return rol,w-num%w

w,m,n=list(map(int,input().split()))
rcm=rc(w,m)
rcn=rc(w,n)
disp=abs(rcm[0]-rcn[0])+abs(rcm[1]-rcn[1])
print(disp)