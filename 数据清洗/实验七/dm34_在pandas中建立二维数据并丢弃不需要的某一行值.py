import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3],[4,5,6]],
                  columns=['col1','col2','col3'],
                  index=['a','b']
)
print(df)
df = df.reindex(['a','b','c','d'])
df = df.drop('a')
print(df)