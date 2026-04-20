def card():
    s=dict.fromkeys(['0','1.机器学习概述','2','3','4','5','6','7','8','9'],3)
    num=0
    while True:
        num+=1
        for c in s:
            if c in str(num):
                cnt=str(num).count(c)
                if s[c]>=cnt:
                    s[c]-=cnt
                else:
                    print(num-1)
                    return
# print(s)
card()#3181