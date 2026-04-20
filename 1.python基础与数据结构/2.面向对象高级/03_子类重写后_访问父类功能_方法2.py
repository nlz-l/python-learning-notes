# 1.机器学习概述.父类名.父类函数名(self)
# 2. super().父类函数名()
class Master:
    def __init__(self):
        self.kongfu = ['古法煎饼果子配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子配方')
class School:
    def __init__(self):
        self.kongfu = ['School煎饼果子配方']
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子配方')

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = ['独创煎饼果子配方']

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子配方')

    def make_old_cake(self):
        super().__init__()
        super().make_cake()


if __name__ == '__main__':
    p = Prentice()
    print(p.kongfu)
    p.make_cake()
    p.make_old_cake()