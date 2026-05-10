from 学生管理系统.student import Student

s1 = Student("myy","女",21,'111','傻子')
print(s1)

my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))
print('-'*23)

s1 = Student("m","女",21,'111','傻子')
s2 = Student("my","女",21,'111','傻子')
s3 = Student("myy","女",21,'111','傻子')
stu_list = [s1,s2,s3]

#列表推导式
list_dict =[stu.__dict__ for stu in stu_list]
print(list_dict)
print('-'*23)

s5 = Student(**my_dict)
print(s5)