def quick_sort(my_list,start,end):
    if start >= end:
        return
    left = start
    right = end
    mid = my_list[start]
    while left < right:
        while my_list[right] >= mid and left < right:
            right -= 1
        my_list[left] = my_list[right]
        while my_list[left] <= mid and left < right:
            left += 1
        my_list[right] = my_list[left]
    my_list[left] = mid

    quick_sort(my_list,start,left)
    quick_sort(my_list,right+1,end)


if __name__ == '__main__':
    my_list =[11, 3, 22, 66, 55]
    print(f'排序前: {my_list}')
    quick_sort(my_list,0,len(my_list)-1)
    print(f'排序后: {my_list}')