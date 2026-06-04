import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

font_set = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=15)
x = np.arange(10)
y = np.random.randint(0, 20, 10)
plt.bar(x, y)
plt.show()