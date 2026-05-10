def my_decorator(fn_name):
    def fn_inner():
        print("正在努力计算中...")
        fn_name()
    return fn_inner

@my_decorator
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f'sum求和结果:{sum}')

get_sum()