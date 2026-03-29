class Car():
    def __init__(self,color,number):
        """
        #该魔法方法用于給 汽车类 对象的属性 赋值
        :param color: 车的颜色
        :param number: 车的轮胎数
        """
        self.color = color
        self.number = number
    def __str__(self):
        return f'颜色:{self.color},轮胎数:{self.number}'

c1 = Car("绿色",4)
print(c1) #默认调用该对象 所在类的str魔法方法