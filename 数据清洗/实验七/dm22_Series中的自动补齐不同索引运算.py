import pandas as pd

s1 = pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])
s2 = pd.Series([6, 7, 8, 9],index=['b', 'c', 'd', 'a'])
print(s1+s2)