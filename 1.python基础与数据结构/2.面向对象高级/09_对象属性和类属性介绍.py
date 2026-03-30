# 对象属性 定义到 init魔法方法
#类属性    函数外的属性

class Student:

    teacher_name = "水镜先生"

    def __init__(self,name,age):
        self.name= name
        self.age = age

    def __str__(self):
        return f'姓名:{self.name},age:{self.age}'

if __name__=='__main__':
    s1 = Student('曹操',38)
    s2 = Student('曹操',38)
    s1.name = '许褚'
    s1.age = 40
    print(f's1:{s1}')
    print(f's2:{s2}')
    print('-' * 23)
    print(s1.teacher_name)
    print(Student.teacher_name)
    print('-' * 23)

    s1.teacher_name = "小丑"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Student.teacher_name)
    print('-' * 23)

    Student.teacher_name = "大丑"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Student.teacher_name)