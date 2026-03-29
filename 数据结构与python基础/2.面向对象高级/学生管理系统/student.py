# 学生类

class Student:
    def __init__(self,name,gender,age,phone,desc):
        """
        该魔法方法用于初始化 属性信息
        :param name: 学生姓名
        :param gender: 性别
        :param age: 年龄
        :param phone: 手机号
        :param desc: 描述性息
        """
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.desc=desc

    def __str__(self):
        """
        该魔法方法, 用于打印学生信息
        :return:
        """
        return f'姓名:{self.name},性别:{self.gender},年龄:{self.age},手机号:{self.phone},描述信息:{self.desc}'

