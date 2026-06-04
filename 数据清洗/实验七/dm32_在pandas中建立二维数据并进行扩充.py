import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3],[4,5,6]],
                  columns=['col1','col2','col3'],
                  index=['a','b'])
df['col4'] = np.array([7,8])
print(df)