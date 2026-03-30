class Animal: #抽象类(也叫:接口)

    def speak(self): #抽象方法
        pass

class Dog(Animal):
    def speak(self):
        print('狗叫:汪汪汪')

class Cat(Animal):
    def speak(self):
        print('猫叫:喵喵喵')

class Car:
    def speak(self):
        print('车叫:嘀嘀嘀')

def make_noise(an:Animal):
    an.speak()

if __name__ == '__main__':
    d = Dog()
    c = Cat()

    make_noise(d)
    make_noise(c)

    e = Car()
    make_noise(e)
