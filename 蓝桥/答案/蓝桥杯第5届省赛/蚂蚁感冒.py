# def isLiveall(l):
#     for c in l:
#         if c!=0:
#             return False
#         else:
#             return True
            
# n=eval(input())#n只蚂蚁
# speed=1#速度1cm/s
# mas=list(map(int,input().split()))#蚂蚁位置
# ganmao=[mas[1]]#第一只蚂蚁感冒了
# length=100#杆子总长100cm
# while isLiveall(mas):
#     for i in range(n):
#         index=mas.index(ganmao[i])
#         if ganmao[i]>0:
#             for j in range(index,n):
#                 if mas[j]<0:
#                     ganmao.append(mas[j])
#                     s=abs(ganmao[i]-mas[j])
#                     t=s/2
#                     for k in range(n):#更新蚂蚁位置
#                         if mas[k]>0 and mas[k]<100:
#                             mas[k]=mas[k]+t
#                         elif mas[k]<0 and abs(mas[k])>0:
#                             mas[k]=mas[k]-t
#                     mas[index]=-mas[index]#更新mas中感冒蚂蚁的方向
#                     mas[j]=-mas[j]#更新mas中被感冒蚂蚁的方向
#                 break#退出循环，进入下一次更新
#         if ganmao[i]<0:
#             for j in range(index):
#                 if mas[j]>0:
#                     ganmao.append(mas[j])
#                     s=abs(ganmao[i]-mas[j])
#                     t=s/2
#                     for k in range(n):#更新蚂蚁位置
#                         a=mas[k]+t
#                         #离开杆子的，置为0
#                         if a>0 and mas[k]<0:
#                             mas[k]=0
#                         if a>100 and 0<mas[k]<100:
#                             mas[k]=0
#                         elif mas[k]==0:
#                             mas[k]=mas[k]
#                         else:
#                             mas[k]=a
#                     mas[index]=-mas[index]#更新mas中感冒蚂蚁的方向
#                     mas[j]=-mas[j]#更新mas中被感冒蚂蚁的方向
#                 break#退出循环，进入下一次更新

   #相当于蚂蚁碰头没有感染
   # 100分 
n=int(input())
mas=list(map(int,input().split()))
ganmao=abs(mas[0])
count=1
for c in mas:
    if 0<c<ganmao or c<-ganmao:
        count+=1
print(count)
