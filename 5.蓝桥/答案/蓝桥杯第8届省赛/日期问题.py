'''
限制：
年：0-59：2000-2059;60-99;1960-1999
月：01-12
日：01-31
 但是 01、03、05、07、08、10、12月有31天
 其余30天
 闰年的2月有29
 其余28天
'''
years1=['0' for _ in range(60)]
years2=[str(i) for i in range(60,100)]
for i in range(60):
    if i<10:
        years1[i]='0'+str(i)
    else:
        years1[i]=str(i)
def ifyear(y): 
    if y in years1:
        return '20'+y
    elif y in years2:
        return '19'+y
    else:
        return y
def ifday(y,m,d):#传入年份，月份和天数
    m1=['01','03','05','07','08','10','12']
    m2=['04','06','09','11']#单独剔除2月
    if d=='00':
        return '0'
    else:
        da=int(d)
        y=int(y)
        if m in m1:
            if da<=31:
                return d
            else:
                return '0'
        elif m in m2:
            if da<=30:
                return d
            else:
                return '0'
        elif m=='02':
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                if da<=29:
                    return d
            else:
                if da<=28:
                    return d
                else:
                    return '0'
        else:
            return  '0'

date=input().split('/')#将输入的日期拆分为列表
time=[]
time2=[]

#年-月-日
if date[1] in ['01','02','03','04','05','06','07','08','10','11','12']:
    month=date[1]
    year=ifyear(date[0])
    day=ifday(year,month,date[2])
else:
    year='0'
    month='0'
    day='0'
time.append([year,month,day])

#月-日-年
if date[0] in ['01','02','03','04','05','06','07','08','10','11','12']:
    month=date[0]
    year=ifyear(date[2])
    day=ifday(year,month,date[1])
else:
    year='0'
    month='0'
    day='0'
time.append([year,month,day])

#日-月-年
if date[1] in ['01','02','03','04','05','06','07','08','10','11','12']:
    month=date[1]
    year=ifyear(date[2])
    day=ifday(year,month,date[0])
else:
    year='0'
    month='0'
    day='0'
time.append([year,month,day])
for i in range(3):
    if len(''.join(time[i]))==8:
        time2.append(time[i])
time3=[]
[time3.append(i) for i in time2 if not i in time3]
time3.sort()
for i in range(len(time3)):
    print('{}-{}-{}'.format(time3[i][0],time3[i][1],time3[i][2]))



