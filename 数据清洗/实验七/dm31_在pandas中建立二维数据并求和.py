import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3],[4,5,6]],
                  columns=['col1','col2','col3'],
                  index=['a','b']
                  )
print(df)
print('\n')
print(df.sum())
print('\n')
print(df - 2)
print('\n')
print(df*2)
print('\n')
print(df/2)