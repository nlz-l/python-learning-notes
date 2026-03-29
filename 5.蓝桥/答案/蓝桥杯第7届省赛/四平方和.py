import math
def si(N):
    n=int(math.sqrt(N)+1)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if pow(i,2)+pow(j,2)+pow(k,2)+pow(l,2)==N:
                        s[0],s[1],s[2],s[3]=i,j,k,l
                        return s
N=int(input())
s=[0 for _ in range(4)]
s=si(N)
# s.sort()
s=[str(c) for c in s]
print(' '.join(s))