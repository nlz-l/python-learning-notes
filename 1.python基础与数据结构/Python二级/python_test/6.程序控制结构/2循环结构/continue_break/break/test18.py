#braek 用来终止所在的循环

#输出1-100之间的前三个偶数

count = 0 #记次数
i = 0
while i < 100:
    i += 1
    if i % 2 ==0:
        print(i)
        count = count + 1
    if count == 3:
        break
