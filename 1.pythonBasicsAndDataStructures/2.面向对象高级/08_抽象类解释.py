class AC:
    def cool_wind(self):
        #制冷
        pass
    def hot_wind(self):
        #制热
        pass
    def swing_l_r(self):
        #左右摆风
        pass

class XiaoMi(AC):
    def cool_wind(self):
        # 制冷
        print('小米 核心 制冷技术!')

    def hot_wind(self):
        # 制热
        print('小米 核心 制热技术!')

    def swing_l_r(self):
        # 左右摆风
        print('小米 核心 静音左右摆风技术!')

class Gree(AC):
        def cool_wind(self):
            # 制冷
            print('格力 核心 制冷技术!')

        def hot_wind(self):
            # 制热
            print('格力 核心 制热技术!')

        def swing_l_r(self):
            # 左右摆风
            print('格力 核心 低频左右摆风技术!')

if __name__ == '__main__':
    xm = XiaoMi()
    xm.cool_wind()
    xm.hot_wind()
    xm.swing_l_r()
    print('-' * 23)
    Gr = Gree()
    Gr.cool_wind()
    Gr.hot_wind()
    Gr.swing_l_r()
