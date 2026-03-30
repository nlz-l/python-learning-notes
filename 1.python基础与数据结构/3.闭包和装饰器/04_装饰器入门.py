# 嵌套 引用 返回 有额外功能
"""
用法
1:
    装饰后的函数名 = 装饰器名(被装饰的原函数名)
    装饰后的函数名()
2:
    在要被装饰的原函数上,直接写 @ 装饰器名, 之后直接调用原函数即可
"""
def check_login(fn_name):
    def fn_inner():
        print('检验登录...登录成功!')

        fn_name()
    return fn_inner


def comment():
    print("发表评论")

@check_login
def payment():
    print('充值中...')

comment1 = check_login(comment)
comment1()
print('-' * 23)
comment()
print('-' * 23)
# 语法糖
payment()

class Student:
    @staticmethod
    def show():
        print('我是静态方法!')
