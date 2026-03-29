def istime(month,day):
    year=int((month+day)[::-1])
    day=int(day)
    if month in ['01','03','05','07','08','10','12']:
        if 1<=day<=31:
            return True
        else:
            return False
    elif month=='02':
        if (year%4==0 and year%100!=0) or (year%400==0):
            if 1<=day<=29:
                return True
            else:
                return False
        else:
            if 1<=day<=28:
                return True
            else:
                return False
    elif month in ['04','06','09','11']:
        if 1<=day<=30:
            return True
        else:
            return False
    else:
        return False
#90分
time=int(input()[0:4])
#回文日期
for i in range(time+1,10000):
        i=str(i)
        temp=i[::-1]
        month=temp[0:2]
        day=temp[2:4]
        if istime(month,day):
            print("{}{}".format(i,i[::-1]))
            break
        else:
            continue
#ABABBABA
for i in range(time+1,10000):
    i=str(i)
    temp=i[::-1]
    month=temp[0:2]
    day=temp[2:4]
    if len(set(i)) == 2 and i[0]==i[2] and i[1]==i[3]:
        if istime(month,day):
            print("{}{}".format(i,i[::-1]))
            break
        else:
            continue 