"""
闭包解释:
    内部函数 使用了外部函数的变量, 这种写法称之为闭包
    格式:
        def 外部函数名(形参列表):
            外部函数名(局部)变量

            def 内部函数名(形参列表):
                使用外部函数列表
            return 内部函数名

细节: 函数名 和函数名()是两个概念
     前者表示 函数对象 后者表示 调用函数, 获取返回值
前提条件:
    1.机器学习概述.嵌套,2.引用,3.返回
"""
def get_sum(a,b):
    return a + b
print(get_sum) # <function get_sum at 0x0000017C431D3240> 对象
print(get_sum(10,20))# 30
my_sum = get_sum
print(my_sum) # <function get_sum at 0x0000022FA0D03240>
print(my_sum(10,20)) # 30
print('-' * 23)

# 演示闭包写法

def fn_other(num1):
    def fn_inner(num2):
        sum = num1 + num2
        print(f"求和结果:{sum}")
    return fn_inner

f = fn_other(10)
f(20)
f(20)
f(20)
print('-' * 23)

fn_other(100)(200)