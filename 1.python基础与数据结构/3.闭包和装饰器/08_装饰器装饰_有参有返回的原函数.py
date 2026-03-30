def my_decorator(fn_name):
    def fn_inner(x,y):
        print("正在计算中...")
        return fn_name(x,y)
    return fn_inner

@my_decorator
def get_sum(a,b):
    return a + b

print(get_sum(1,2))