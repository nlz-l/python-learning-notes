class Car:
    #属性

    #行为
    def run(self):
        print("汽车会跑！...")
        print(f'我是run函数，self的值为：{self}')

c1 = Car()
print(f'c1对象：{c1}')
c1.run()
print('-'*34)

c2 = Car()
print(f'c1对象：{c2}')
c2.run()
print('-'*34)