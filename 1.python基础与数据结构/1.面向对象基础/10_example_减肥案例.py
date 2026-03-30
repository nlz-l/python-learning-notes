class student:
    def __init__(self):
        self.current_weight = 100

    def run(self):
        print("疯狂跑步...")
        self.current_weight -= 0.5

    def eat(self):
        print('大吃大喝一顿...')
        self.current_weight += 2

    def __str__(self):
        return f'当期体重:{self.current_weight}'

#测试
if __name__ == '__main__':
    xm = student()
    #跑步
    xm.run()
    #吃喝
    xm.eat()
    #当前体重
    print(xm)