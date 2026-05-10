def my_decorator(fn_name):
    def fn_inner(*x,**y):
        print("正在努力计算中...")
        return fn_name(*x,**y)
    return fn_inner

@my_decorator
def get_sum(*args,**kwargs):
    """
    该函数用于计算 数字列表 和 字典value值 之和
    :param args: 数字元组  *args 接收所有的位置参数, 封装到 元组
    :param kwargs: 字典,键是字符串值是数字 **kwargs 接收所有的关键字参数,封装到 字典
    :return: 结果之和
    """
    sum = 0
    for i in args:
        sum += i

    for v in kwargs.values():
        sum += v
    return sum

    #return sum(args) + sum(kwargs.values())

sum = get_sum(1,2,3,4,5,6,a=7,b=8,c=9)
print(sum)

