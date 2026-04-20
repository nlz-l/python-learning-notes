def bubble_sort(my_list):    #稳定算法
    n = len(my_list)
    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                count += 1
                my_list[j] , my_list[j + 1] = my_list[j + 1] , my_list[j]
        print(f'第{i + 1}轮排序次数：{count}')
        if count == 0:
            break

if __name__ == '__main__':
    my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #my_list = [1.机器学习概述, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bubble_sort(my_list)
    print(my_list)
