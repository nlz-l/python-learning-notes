# b=[]
# for i in range(2):
#     for j in range(3):
#         b.append([i,j])
# print(b)
'''
斜率：k = (y2 - y1) / (x2 - x1)
截距：b = - k * x1 + y1 = (x2 * y1 - x1 * y2) / (x2 - x1)
'''
x, y = map(int, input().split())
points = [[i, j] for i in range(x) for j in range(y)]  # 每个点的坐标
line = set()  # 用来存储每条线的斜率和截距
for i in range(len(points) - 1):
    x1, y1 = points[i][0], points[i][1]
    for j in range(i, len(points)):
        x2, y2 = points[j][0], points[j][1]
        if x1 == x2:  # 当斜率为无穷时不进行计算，斜率为无穷时直线个数为x
            continue
        k = (y2 - y1) / (x2 - x1)
        b = (x2 * y1 - x1 * y2) / (x2 - x1)
        if (k, b) not in line:
            line.add((k, b))  # 利用元组不可变的性质，可以直接存入集合中
print(len(line) + x)  # 加上斜率为无穷时的直线个数x
