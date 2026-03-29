n = int(input())
h=int(n/(1000*60*60))
HH=h%24

m=n-h*1000*60*60
MM=int(m/(1000*60))

s=m-MM*1000*60
SS=int(s/1000)

print("{:0>2}:{:0>2}:{:0>2}".format(HH,MM,SS))