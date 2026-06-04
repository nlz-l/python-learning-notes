import numpy as np
import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6]],
                  columns=['col1','col2','col3'],
                  index=['a','b']
)
print(df)
print('\n')
df = df.reindex(['a','b','c','d'])
print(df)