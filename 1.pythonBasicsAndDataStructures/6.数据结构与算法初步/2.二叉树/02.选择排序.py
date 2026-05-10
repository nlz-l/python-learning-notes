def select_sort(my_list):      #不稳定算法
    n = len(my_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            my_list[i] ,my_list[min_index] = my_list[min_index] , my_list[i]


if __name__ == '__main__':
    my_list = [5, 4, 3, 2, 2]
    # my_list = [1.机器学习概述, 2, 3, 4, 5]
    select_sort(my_list)
    print(my_list)