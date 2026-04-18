i,j,num=0,0,0
while True:
    # print(i,j)
    num+=1
    if i==19 and j==19:
        print(num)#761
        break
    else:
        if i==0:#在x轴上
            if j%2==0:
                j+=1
            else:
                i+=1
                j-=1
        elif j==0:#在y轴上
            if i%2!=0:
                i+=1
            else:
                i-=1
                j+=1
        else:#在中间的部分
            if (i+j)%2==0:#横纵坐标相加为偶数
                i-=1
                j+=1
            else:#横纵坐标相加为奇数
                i+=1
                j-=1