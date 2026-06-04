import pandas as pd

data = {'name':['leslie','amos','bill','bert'],
        'year':['1980','1986','1988','1990'],
        }
frame2 = pd.DataFrame(data,columns=['year','name'])
print(frame2)