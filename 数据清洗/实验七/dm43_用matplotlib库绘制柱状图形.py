import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=15)
x = [0,1,2,3,4,5]
y = [1,2,3,2,4,3]
plt.bar(x,y)
plt.title('柱状图',fontproperties=font_set)
plt.xlabel("x轴",fontproperties=font_set)
plt.ylabel("y轴",fontproperties=font_set)
plt.show()