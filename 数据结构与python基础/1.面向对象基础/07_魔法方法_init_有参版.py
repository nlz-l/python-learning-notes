class Car():
    def __init__(self,color,number):
        """
        #该魔法方法用于給 汽车类 对象的属性 赋值
        :param color: 车的颜色
        :param number: 车的轮胎数
        """
        self.color = color
        self.number = number

    def show(self):
        print(f'颜色:{self.color},轮胎数:{self.number}')
c1 = Car("红色",4)
c1.show()
print("-"*23)
c2 = Car("绿色",6)
c2.show()
print("-"*23)
