from datetime import *
n = int(input())
for _ in range(n):
    A,B,C = input().split()
    time = datetime.strptime(A + " " + B,'%Y-%m-%d %H:%M:%S')
    X = int(C)
    delta = time - datetime(1970,1,1,0,0,0)
    d = (delta.total_seconds() // 60) % X
    finaltime = time - timedalta(minutes = d)
    print(finaltime.replace(second=0))
