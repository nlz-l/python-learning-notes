def insert_sort(my_list):  #稳定算法
    n = len(my_list)
    for i in range(1, n):
        for j in range(i,0,-1):
            if my_list[j] < my_list[j - 1]:
                my_list[j] , my_list[j - 1] = my_list[j - 1] , my_list[j]
            else:
                 break


if  __name__ == '__main__':
    # my_list = [5, 4, 3, 2, 1.机器学习概述]
    my_list = [1, 2, 3,3, 4, 5]
    insert_sort(my_list)
    print(my_list)