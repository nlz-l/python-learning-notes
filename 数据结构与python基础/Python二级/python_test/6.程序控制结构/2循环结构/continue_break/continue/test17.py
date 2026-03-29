#continue 结束当前本次循环 continue 后面的内容不会执行，然后继续执行下一次循环

# 输出1-100之间的所有偶数

i = 0
while i < 100:
    i += 1
    if i % 2 == 1: #为奇数时，跳过
        continue
    print(i)
