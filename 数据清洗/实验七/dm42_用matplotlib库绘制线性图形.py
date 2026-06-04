import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=20)
dataX = [1,2,3,4]
dataY = [2,4,4,2]
plt.plot(dataX,dataY)
plt.title('绘制直线',fontproperties=font_set)
plt.xlabel("x轴",fontproperties=font_set)
plt.ylabel("y轴",fontproperties=font_set)
plt.show()