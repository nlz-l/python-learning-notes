#绝对路径
path1 = "C:/Users/liuwenbo/Desktop/文件夹/python_test/15.文件基本操作/2.文件操作/a/test.txt"
f = open(path1,"rt",encoding ="UTF-8")
s = f.read()
f.close()
print(s)

#相对路径
path2 = "a/test.txt"
f = open(path2,"rt",encoding ="UTF-8")
s = f.read()
f.close()
print(s)

# \n 换行
# \t tab
# \\ \

print("Hello\nWorld")
print("Hello\\World")
