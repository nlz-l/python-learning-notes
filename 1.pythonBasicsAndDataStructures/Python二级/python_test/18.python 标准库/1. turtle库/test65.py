'''
turtle.setup(width, height, startx, starty)
width:窗口宽度
height:窗口高度
startx:窗口与屏幕左侧距离(单位像素)
starty:窗口与屏幕顶部距离(单位像素)
'''
import turtle as t

t.setup(600,600,1000,200)
# 前进forward() fd()
# 后退backward() bk()

#t.fd(100)
#t.bk(100)
# right() 
# left()

for i in range(4):
    t.fd(100)
    t.left(90)
    
