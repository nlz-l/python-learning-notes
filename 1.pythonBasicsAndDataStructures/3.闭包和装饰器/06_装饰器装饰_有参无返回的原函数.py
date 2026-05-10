def my_decorator(fn_name):
    def fn_inner(x,y):
        print("正在计算中...")
        fn_name(x,y)
    return fn_inner

@my_decorator
def get_sum(a,b):
    sum = a + b
    print(f'sum求和结果:{sum}')


get_sum(10,10)