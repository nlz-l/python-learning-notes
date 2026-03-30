class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = "生的"
        self.condients = []

    def cook(self,time):

        if time < 0:
            print("无效值,请重新录入")
        else:
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_state = "生的"
            elif 3 <= self.cook_time < 7:
                self.cook_state = "半生不熟"
            elif 7 <= self.cook_time < 12:
                self.cook_state = "熟了"
            else:
                self.cook_state = "糊了"

    def add_condiment(self,condient):
        self.condients.append(condient)
    def __str__(self):
        return (f'烘烤时间:{self.cook_time},地瓜状态:{self.cook_state},调料:{self.condients}')
if __name__ == "__main__":
    dg = SweetPotato()
    dg.cook(3)
    dg.cook(5)
    dg.add_condiment("芥末")
    dg.add_condiment("鱼腥草")
    dg.add_condiment("豆汁")
    dg.add_condiment("鲱鱼罐头")

    print(dg)