import pandas as pd

data = {'name':['leslie','amos','bill','bert'],
        'year':['1980','1986','1988','1990'],
        }
frame2 = pd.DataFrame(data,columns=['year','name']
                            ,index=['one','two','three','four'])
print(frame2)
print('one' in frame2.index)
print('five' in frame2.index)

