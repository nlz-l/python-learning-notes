class HeroFighter: #英雄1代
    def power(self):
        return 60
class AdvHeroFighter(HeroFighter):  #英雄2代
    def power(self):
        return 80
class EnemyFighter:  #敌机1代
    def power(self):
        return 70
# 多态
def object_play(hero:HeroFighter,enemy:EnemyFighter):
    if hero.power() >=enemy.power():
        print("英雄机 战胜 敌机")
    else:
        print("英雄机 惜败 敌机")
if __name__ == '__main__':
    #1不用多态
    # H1 = HeroFighter()
    # E1 = EnemyFighter()
    # if H1.power() >= E1.power():
    #     print("英雄机1代 战胜 敌机1代")
    # else:
    #     print("英雄机1代 惜败 敌机1代")
    # print("-"*23)
    # H2 = AdvHeroFighter()
    # E1 = EnemyFighter()
    # if H2.power() >= E1.power():
    #     print("英雄机2代 战胜 敌机1代")
    # else:
    #     print("英雄机2代 惜败 敌机1代")
    # print("-" * 23)

    #2 多态
    h1 = HeroFighter()
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    object_play(h1,e1)
    object_play(h2,e1)
    object_play(h1,h2)