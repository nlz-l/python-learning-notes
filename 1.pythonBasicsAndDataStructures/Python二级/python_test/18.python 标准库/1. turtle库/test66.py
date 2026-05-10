import turtle as t

t.setup(600,600,1000,200)
t.pensize(2)# 别名width() 画笔粗细
#t.pencolor("blue") #画笔颜色 pencolor((r,g,b)) 0~1.机器学习概述
t.pencolor((1,0.5,0.5))
t.color("red",(1,0.5,0.5))
t.begin_fill()# 开始填充
t.hideturtle()# 隐藏画笔
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()# 结束填充
print(t.filling())# 填充状态
t.showturtle()# 显示画笔
t.write("在画图")
#t.clear()# 清空当前窗口
#t.reset() # 都恢复为默认值



