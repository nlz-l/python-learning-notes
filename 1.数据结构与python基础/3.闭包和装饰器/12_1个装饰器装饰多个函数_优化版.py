
def my_decorator(fn_name):
    def fn_inner(x,y):
        if fn_name.__name__ == 'get_sum':
            print('正在努力计算[加法]中...')
        elif fn_name.__name__ == 'get_sub':
            print('正在努力计算[减法]中...')
        return fn_name(x,y)
    return fn_inner


@my_decorator
def get_sum(a,b):
    return a+b
@my_decorator
def get_sub(a,b):
    return a-b

print(get_sum(3,2))
print(get_sub(3,2))