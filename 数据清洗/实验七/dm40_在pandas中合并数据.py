import numpy as np
import pandas as pd

data1 = pd.DataFrame({'level1':['a','b','c','d'],
                      'number1':[1,3,5,7]})
data2 = pd.DataFrame({'level2':['a','b','c','e'],
                      'number2':[2,4,6,8]})
print(pd.merge(data1,data2,left_on='level1',right_on='level2'))