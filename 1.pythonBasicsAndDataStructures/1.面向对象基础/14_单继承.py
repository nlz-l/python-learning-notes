class Master:
    def __init__(self):
        self.kongfu ="[古法配方]"
    def make_cake(self):
        print(f'采用 {self.kongfu} 摊煎饼果子')

class Prentice(Master):
    pass

p = Prentice()
p.make_cake()