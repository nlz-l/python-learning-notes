class Car:
    #属性

    #行为
    def run(self):
        print(f"{self} 汽车在跑...")
    def work(self):
        print(f"我是work函数，我的self值为:{self}")
        self.run()
c1=Car()
print(f"c1对象：{c1}")
c1.run()
print("-"*34)
c1.work()
print("="*34)

c2 = Car()
print(f"c2对象：{c2}")
c2.run()
print("-"*34)
c2.work()