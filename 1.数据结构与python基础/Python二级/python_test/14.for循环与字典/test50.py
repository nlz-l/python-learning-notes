d = {"2001101":"刘备","2001102":"关羽","2001103":"张飞","2001104":"赵云"}

for i in d.keys():
    print(i)

for i in d.keys():
    print(d[i])
    
for i in d.values():
    print(i)

for i in d.items():
    print(i)
    print(type(i))# <class 'tuple'>
    print(i[0],i[1])

for k,v in d.items():
    print(k,v)
