def my_decorator(fn_name):
    def fn_inner():
        print("正在计算中...")
        return fn_name()
    return fn_inner

@my_decorator
def get_sum():
    a = 10
    b = 20
    return a + b

print(get_sum())