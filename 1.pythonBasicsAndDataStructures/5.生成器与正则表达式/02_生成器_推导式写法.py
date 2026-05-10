import sys

my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))
print('-' * 23)

my_g2 = (i for i in range(1,11) if i % 2 == 0)
print(my_g2)
print(type(my_g2))

print(next(my_g2)) # 2
print(next(my_g2)) # 4
print('-' * 23)

for i in my_g2:
    print(i)   # 6  8  10

my_list =[i for i in range(10000000)]
my_gt3 =(i for i in range(10000000)) #生成器
print(type(my_list),type(my_gt3))
print(f'my_list的内存占用: {sys.getsizeof(my_list)}')
print(f'my_gt3的占用内存: {sys.getsizeof(my_gt3)}')
print('-' * 23)

