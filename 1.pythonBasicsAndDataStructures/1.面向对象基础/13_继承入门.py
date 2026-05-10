class Father:
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print("饭后走一走,能活九十九!")
    def smoking(self):
        print("抽烟有害健康")
class Son(Father):
    pass

s = Son()
print(f'性别:{s.gender}')
s.walk()
s.smoking()