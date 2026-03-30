try:
    a = 5
    b = 0
    print(a/ b)
except ZeroDivisionError:
    print("这里不能除以零. . .")
except:
    print("出错了")
