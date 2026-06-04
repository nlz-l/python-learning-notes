import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(6))
s[::2]=np.nan
print(s)