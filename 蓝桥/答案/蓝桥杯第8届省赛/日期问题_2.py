#日期问题
n = input()
list1 = []
a = n.split("/")
def wang1(x,y,z):
    if int(y)!=2:
        if int(y) in [1,3,5,7,8,10,12] and int(z) <= 31:
            list1.append("20%s-%s-%s" % (x, y, z))
        elif int(y) in [4,6,9,11] and int(z)<=30:
            list1.append("20%s-%s-%s" % (x, y, z))
    if int(y)==2:
        if (int("20%s"%x)%4==0 and int("20%s"%x)%100!=0) or int("20%s"%x)%400==0:
            if int(z)<=29:
                list1.append("20%s-%s-%s"%(x,y,z))
        elif int(z)<=28:
            list1.append("20%s-%s-%s" % (x, y, z))
def wang2(x,y,z):
    if int(y)!=2:
        if int(y) in [1,3,5,7,8,10,12] and int(z) <= 31:
            list1.append("19%s-%s-%s" % (x, y, z))
        elif int(y) in [4,6,9,11] and int(z)<=30:
            list1.append("19%s-%s-%s" % (x, y, z))
    elif (int("19%s"%x)%4==0 and int("19%s"%x)%100!=0) or int("19%s"%x)%400==0:
        if int(z)<=29:
            list1.append("19%s-%s-%s"%(x,y,z))
    elif int(z)<=28:
            list1.append("19%s-%s-%s" % (x, y, z))
if 0<int(a[1])<=12 and int(a[0])<=59:
    wang1(x=a[0],y=a[1],z=a[2])
elif 0<int(a[1])<=12 and int(a[0])>59:
    wang2(x=a[0], y=a[1], z=a[2])
if 0<int(a[0])<=12 and int(a[2])<=59 and int(a[1])<=31:
    wang1(x=a[2], y=a[0], z=a[1])
elif 0<int(a[0])<=12 and int(a[2])>59 and int(a[1])<=31:
    wang2(x=a[2], y=a[0], z=a[1])
if 0<int(a[1])<=12 and int(a[2])<=59 and 0<int(a[0])<=31:
    wang1(x=a[2], y=a[1], z=a[0])
elif 0 < int(a[1]) <= 12 and int(a[2]) > 59 and 0<int(a[0])<=31 :
    wang2(x=a[2], y=a[1], z=a[0])
temp = list(set(list1))
temp.sort()
for i in temp:
    print(i)
