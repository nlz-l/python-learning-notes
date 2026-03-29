class Car:
    #属性

    #行为
    def run(self):
        print(f'汽车会跑...')

#类外创建对象
c1 = Car()
c1.run()
c1.color = "red"
c1.number = 4
print(f'颜色:{c1.color},轮胎数:{c1.number}')
print('-'*34)
c2=Car()
c2.run()
#c2不可访问c1里创建的方法
#print(f"颜色:{c2.color},轮胎数:{c2.number}")
