# __init__()  创建对象时，自动触发

class Car:
    def __init__(self):
        print("我是 无参 init 魔法方法")
        self.number = 3
        self.color = "黑色"
    def show(self):
        print(f'颜色:{self.color},轮胎数:{self.number}')

c1 = Car() #自动调用__init__函数
c1.color = "红色"
c1.number = 6
print(c1.color, c1.number)
c1.show()
print(f'-'*34)
c2 = Car()
c2.show()
print(f'-'*34)