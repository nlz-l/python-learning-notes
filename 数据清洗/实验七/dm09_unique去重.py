import numpy as np

arr = np.array([3,4,5,7,8,4,6,2,4,])
print('第一个数组',arr)
print('去掉重复数据后的值')
arr_a = np.unique(arr)
print(arr_a)