import pandas as pd

data = {'name':['leslie','amos','bill','bert'],
        'year':['1980','1986','1988','1990'],
        }
pop = {'leslie':{1980},'amos':{1986}}
frame3 = pd.DataFrame([pop])
print(frame3)