
def logging(flag):
    def my_decorator(fn_name):
        def fn_inner(x,y):
            if flag == '+':
                print('正在努力计算[加法]中...')
            elif flag == '-':
                print('正在努力计算[减法]中...')
            return fn_name(x,y)
        return fn_inner
    return my_decorator

@logging('+')
def get_sum(a,b):
    return a+b
@logging('-')
def get_sub(a,b):
    return a-b


print(get_sum(2,3))
print(get_sub(3,2))