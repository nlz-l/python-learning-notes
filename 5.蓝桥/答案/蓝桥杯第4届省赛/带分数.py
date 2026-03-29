a = input('')
a_num = int(a)
count = 0
# print(int('9'*(5-len(a)))+int('9'*(6-len(a))))
for i in range(int('9'*(5-len(a))), int('9'*(6-len(a)))):
    # print(i)
    for n in range(1, a_num):
        stra = str(n) + str((a_num - n)*i) + str(i)
        # print(n, (a_num - n)*i, i)
        for j in range(9):
            if str(j+1) not in stra:
                j = 7
                break
        if j == 8 and len(stra) == 9:
            # print(stra)
            # print(n, (a_num - n)*i, i)
            count += 1
        # print(stra)
print(count)

