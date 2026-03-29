# 自定义的类中 只要有: __iter__  __next__ 就称为迭代器

for i in range(1,6):
    print(i)
print('-' * 23)

class MyIterator:
    def __init__(self,start,end):
        self.current_value = start
        self.end = end
    def __iter__(self): #返回当前对象 即迭代器对象
        return self
    def __next__(self): #返回当前值 并更新当前值
        if self.current_value >= self.end:
            raise StopIteration
        # value = self.current_value
        # self.current_value += 1
        # return value
        #效果同上
        self.current_value += 1
        return self.current_value - 1




for i in MyIterator(1,6):
    print(i)
print('-' * 23)
my_itr = MyIterator(10,13)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
