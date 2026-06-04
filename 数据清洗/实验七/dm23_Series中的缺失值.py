import pandas as pd

s1 = pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])
s2 = pd.Series([6, 7, 8],index=['b', 'c', 'd'])
print(s1+s2)