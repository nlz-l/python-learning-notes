#冒泡排序交换公式：count=(n*(n-1))/2
#就是n=15 结合题目
#abcdefghijklmno
#倒着写：onmlkjihgfedcba 交换成正序最多105次
#要求100次，则手动交换5次
#o向后还5次，把j换到最前面：jonmlkihgfedcba
#验证是不是100次
s=list('jonmlkihgfedcba')
cnt=0
for i in range(len(s)-1):
    for j in range(len(s)-1-i):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
            # print(s)
            cnt+=1
print(cnt)