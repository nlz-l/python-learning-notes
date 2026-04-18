n,m=input().split(' ')
def fanyingbi(n,m):
    if len(n) % 2 == 0:
        n_len = len(n) / 2
    else:
        n_len = (len(n) // 2) + 1
    n_len = int(n_len)
    n_1 = []
    n_2 = []
    for i in range(n_len):#构建全为0的列表模拟平方根
        n_1.append('0')
    for i in range(n_len):
        n_2.append('0')
    for x in range(n_len):
        for y in range(1, 10):
            n_1[x] = str(y)#将（1-9）插入x位置
            n_2[x] = str(y - 1)#由于减了1，也不会漏掉0的情况
            a = ''.join(n_1)#字符串化
            b = ''.join(n_2)
            if eval(a) ** 2 > eval(n) and eval(b) ** 2 <= eval(n):#当x位上的数字满足条件时，跳出循环
                break
    n_sum = eval(''.join(n_2))

if len(m) % 2 == 0:
    m_len = len(m) / 2
else:
    m_len = (len(m) // 2) + 1

m_len = int(m_len)
m_1 = []
m_2 = []

for i in range(len(n)):#构建全为0的列表模拟平方根
    m_1.append('0')
for i in range(len(n)):
    m_2.append('0')
for x in range(m_len):
    for y in range(1, 10):
        m_1[x] = str(y)#将（1-9）插入x位置
        m_2[x] = str(y - 1)#同时不要忘记0的情况
        a = ''.join(m_1)#字符串化
        b = ''.join(m_2)
        if eval(a) ** 2 > eval(n) and eval(b) ** 2 <= eval(n):#当平方根满足条件时，跳出循环
            break

m_sum=eval(''.join(m_2))
print(m_sum)