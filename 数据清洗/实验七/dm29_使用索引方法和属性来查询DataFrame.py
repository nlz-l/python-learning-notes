import pandas as pd

data = {'name':['leslie','amos','bill','bert'],
        'year':['1980','1986','1988','1990'],
        }
pop = {'leslie':{1980},'amos':{1986}}
frame2 = pd.DataFrame(data,columns=['year','name'])
print(frame2)
print('1980' in frame2.columns)
print('name' in frame2.columns)