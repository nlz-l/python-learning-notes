import datetime
start = datetime.date(2000,1,1)
end = datetime.date(2020,10,1)
days = datetime.timedelta(days = 1)
count = 0
while start <=end:
    if start.weekday() == 0 or start.day == 1:
        count += 2
    else:
        count += 1
    start += days
print(count) ##8879

'''
sj = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A') #2025-12-09 18:33:21 Tuesday
print(sj)
'''