import pandas as pd
import numpy as np

df = pd.read_csv("./python数据清数据/test.csv")
print(df)
print('\n')
print(df.fillna('miss'))
print('\n')
print(df.fillna(10))
print('\n')
print(df.ffill())
print('\n')
print(df.dropna())