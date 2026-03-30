a =2025
count = 0
while(a>0):
  count+=1
  a-=5
  if(count%2==0):
    a-=2
  else:
    a-=15
  if(count%3==1):
    a-=2
  elif(count%3==2):
    a-=10
  else:
    a-=7
print(count)
