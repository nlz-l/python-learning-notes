# 学生管理系统 增删改查
import time
from student import Student

class StudentCMS(object):
    def __init__(self):
        #存储学生信息
        self.stu_list = []
    @staticmethod
    def show_view():
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.机器学习概述.添加学生信息')
        print('\t2.修改学生信息')
        print('\t3.删除学生信息')
        print('\t4.查询某个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*' * 23)
    def add_student(self):

        name = input('请输入学生的姓名:')
        gender = input('请输入学生的性别:')
        age = int(input('请输入学生的年龄:'))
        phone = input('请输入学生的手机号:')
        desc = input('请输入学生的描述信息:')
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f'添加 {name} 学生信息成功!\n')
    def update_student(self):
        update_name = input('请输入要修改学生的姓名:')
        for stu in self.stu_list:
            if stu.name == update_name:
                stu.age = int(input('请输入修改后的年龄:'))
                stu.gender = input('请输入修改后的性别:')
                stu.phone = input('请输入修改后的电话:')
                stu.desc = input('请输入修改后的描述信息:')

                print(f'学生 {update_name} 信息修改成功!')
                break
        else:
            print('查无此人,请检查后重试!\n')
    def del_student(self):
        del_name = input('请输入要删除学生的姓名:')
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f'学生 {del_name} 信息删除成功!')
                break
        else:
            print('查无此人,请检查后重试!\n')
    def search_one_student(self):
        search_name = input('请输入要查找学生的姓名:')
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu,end='\n\n')
                break
        else:
            print('查无此人,请检查后重试!\n')
    def search_all_student(self):
        if len(self.stu_list) == 0:
            print('暂无学生信息,请先添加后查询!\n')
        else:
            for stu in self.stu_list:
                print(stu)
            print()
    def save_student(self): #保存
        with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            dest_f.write(str(stu_dict))
    def load_student(self): #加载
        try:
            with open('./stu_data.txt', 'r', encoding='utf-8') as src_f:
                stu_data = src_f.read()
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open('./stu_data.txt', 'w', encoding='utf-8') as src_f:
                pass
    def start(self):
        self.load_student()
        while True:
            time.sleep(1)
            StudentCMS.show_view()
            input_num = input('请输入您要操作的编号:')
            if input_num == '1.机器学习概述':
                #print("添加学生信息\n")
                self.add_student()
            elif input_num == '2':
                #print("修改学生信息\n")
                self.update_student()
            elif input_num == '3':
                #print("删除学生信息")
                self.del_student()
            elif input_num == '4':
                #print("查询单个学生信息\n")
                self.search_one_student()
            elif input_num == '5':
                #print("查询所有学生信息\n")
                self.search_all_student()
            elif input_num == '6':
                self.save_student()
                print("保存学生信息成功\n")
            elif input_num == '0':
                re = input("您确定要退出吗?(Y/N) -> ")
                if re.lower() == 'y':
                    self.save_student()
                    print("期待您的使用,期待下次再会!")
                    break
            else:
                print("录入有误,请重新录入!\n")

