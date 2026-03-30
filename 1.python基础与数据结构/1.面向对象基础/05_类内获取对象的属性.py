class Car():
    #属性

    #行为
    def run(self):
        print(f'汽车会跑...')
    def show(self):
        print(f'我是show函数，对象的颜色:{self.color}，对象的轮胎数:{self.number}')

c1 = Car()
c1.color = "red"
c1.number = 4

print(f'颜色：{c1.color},轮胎数{c1.number}')
c1.run()
c1.show()

c2 = Car()
#c2.show()  报错 无属性
