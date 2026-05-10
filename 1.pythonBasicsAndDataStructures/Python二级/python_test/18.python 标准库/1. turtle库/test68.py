import turtle as t

t.speed(4)# 画笔速度 越大越快

t.circle(60)
t.circle(-60)
t.circle(60,360)
t.circle(60,-180)
t.circle(60,steps=6)
t.up()
t.goto(60,100)
t.setx(200)
t.sety(0)
t.down()
t.setheading(0) #别名 seth() 设定角度
t.seth(90)
t.dot(50,"red")
