import pandas as pd
import numpy as np

frame = pd.DataFrame([[1,2,3,None],[4,7,None,3],
                      [None,None,None,None]])
print(frame)
print('\n')
frame.info()
print('\n')
# (1)
print(frame.dropna())
print('\n')
# (2)
print(frame.dropna(how='all'))
print('\n')
# (3)
print(frame.isnull())
print('\n')
# (4) (1)
print(frame.fillna(1))
print('\n')
# (4) (2)
print(frame.fillna({0:1,1:2,2:3,3:4}))
