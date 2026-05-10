#property

class Student:

    def __init__(self):
        self.__age = 10

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == '__main__':
    s = Student()
    s.age = 20
    print(s.age)