#时间复杂度:(log n)

def binary_search_recursion(my_list,target):  #递归版
    """

    :param my_list: 待查找列表
    :param target:  要查找列表
    :return:  True在 False 不在
    """
    n = len(my_list)
    if n == 0:
        return False
    mid = n // 2
    if my_list[mid] == target:
        return True
    elif my_list[mid] > target:
        return binary_search_recursion((my_list[: mid]), target)
    else:
        return binary_search_recursion((my_list[mid + 1:]), target)


def binary_search(my_list,target):    #非递归版
    """

        :param my_list: 待查找列表
        :param target:  要查找列表
        :return:  True在 False 不在
        """

    start = 0
    end = len(my_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False




if __name__ == '__main__':
    my_list = [1, 3, 9, 11, 16, 21, 46, 48, 50, 60]
    print(binary_search_recursion(my_list, 25))
    print(binary_search_recursion(my_list, 60))
    print('-' * 23)
    print(binary_search(my_list, 25))
    print(binary_search(my_list, 60))