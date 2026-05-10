#键盘接收
age = input("请您输入年龄：")#接受键盘输入的年龄并赋值给变量age
print(type(age))#<class 'str'>
#年龄计算
age_new = int(age) + 10 #<class 'int'>
print("计算的年龄为：" + str(age_new))
