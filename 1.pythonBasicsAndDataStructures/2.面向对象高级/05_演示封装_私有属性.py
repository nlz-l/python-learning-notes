class Prentice:
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
        self.__money = 20000 #私有
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def get_money(self):  #看
        return self.__money

    def set_money(self, money): #用
        self.__money = money
class TuSun(Prentice):
    pass

if __name__ == '__main__':
    ts = TuSun()
    print(ts.kongfu)
    ts.make_cake()
    ts.set_money(100)
    print(ts.get_money())