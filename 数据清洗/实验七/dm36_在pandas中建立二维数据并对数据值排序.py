import pandas as pd
import numpy as np

df = pd.DataFrame({'b':[3,5,8,-1],'a':[1,4,3,9]})
print(df)
print('\n')
df = df.sort_values(by='a')
print(df)