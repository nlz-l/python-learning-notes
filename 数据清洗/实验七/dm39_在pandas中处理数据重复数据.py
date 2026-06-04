import pandas as pd
import numpy as np
from pandas.core.algorithms import value_counts_internal

frame = pd.DataFrame({'a':['one']*2+['two']*3,'b':[1,1,2,2,3]})
print(frame)
print('\n')
# (1)
print(frame.duplicated().value_counts())
print('\n')
# (2) (1)
print(frame.drop_duplicates())
print('\n')
# (2) (2)
print(frame.drop_duplicates(['a']))