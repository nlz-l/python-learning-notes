#读
# f.read(size)
#从文件中读入整个文件内容。参数可选，如果给出，读入前size长度的字符串或字节流
# f.readline(size)
#从文件中读入一行内容。参数可选，如果给出，读入该行前size长度的字符串或字节流
#f.readlihes (hint)
#从文件中读入所有行，以每行为元素形成一个列表。参数可选，如果给出，读入hint字节数
#f.seek(offset)
#改变当前文件操作指针的位置，
#offset的值：0为文件开头；1为从当前位置开始；2为文件结尾
path = "C:/Users/liuwenbo/Desktop/文件夹/python_test/15.文件基本操作/2.文件操作/a/test.txt"
f1 = open(path,"rt",encoding="UTF-8")
s1 = f1.read()
print(s1)
f1.close()

f2 = open(path,"rb")# 二进制
s2 = f2.read()
print(s2)
f2.close()

f3 = open(path,"rt",encoding="UTF-8")
s3 = f3.readline()
print(s3)
s3 = f3.readline()
print(s3)
s3 = f3.readline(2)
print(s3)
f3.close()


f4 = open(path,"rt",encoding="UTF-8")
s4 = f4.readlines(20) # 字节数
print(s4)# 列表

f4.close()
