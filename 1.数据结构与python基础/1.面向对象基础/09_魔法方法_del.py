class Car:
    def __init__(self,brand):
        self.brand = brand

    def __str__(self):
        return f'品牌:{self.brand}'
    def __del__(self):
        print(f'{self} 对象被删除了！')

c1 =Car("小米 Su7 Ultra")
print(c1)

print(c1.brand)
print('-'*23)

print("程序结束")
