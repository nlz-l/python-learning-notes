class Master:
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
    def make_cake(self):
        print(f'运用{self.kongfu} 制作煎饼果子')
class School:
    def __init__(self):
        self.kongfu = "[学校煎饼果子配方]"
    def make_cake(self):
        print(f'运用{self.kongfu} 制作煎饼果子')
class Prentice(School,Master): #从左往右就近原则
    pass
xm = Prentice()
print(xm.kongfu)
xm.make_cake()
print('-'*23)

#扩展mro机制

print(Prentice.mro()) #Prentice-->School-->Master-->object
print(Prentice.__mro__) #Prentice-->School-->Master-->object