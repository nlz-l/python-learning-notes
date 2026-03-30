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
if __name__ == '__main__':
    p = Prentice()
    print(p.kongfu)
    p.make_cake()