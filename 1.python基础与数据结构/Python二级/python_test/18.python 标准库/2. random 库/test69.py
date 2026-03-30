import random as r

r.seed(10)  #随机数种子 设定随机数
print(r.random()) #生成0.0-1.0（不包含1.0）的随机小数
print(r.random())

print(r.randint(1,10))#生成 a,b 整数

print(r.getrandbits(10))  #getrandbits(10) 生成 k bit 随机整数

print(r.randrange(10,100)) # randrange(start,stop,[step])

print(r.uniform(1,3)) # 生成a,b 随机小数

ls = [12,34,45,23,1,566,123]
print(r.choice(ls))

r.shuffle(ls) #打乱列表
print(ls)

print(r.sample(ls,4)) #在列表中随机选取 n 个元素 以列表返回
