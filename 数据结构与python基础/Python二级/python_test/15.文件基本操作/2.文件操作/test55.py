path1 = "C:/Users/liuwenbo/Desktop/文件夹/python_test/15.文件基本操作/2.文件操作/a/test.txt"
f = open(path1,"rt",encoding ="UTF-8")
ls = f.readlines()
for i in ls:
    print(i,end="")
print()
f.seek(0)
for j in f:
    print(j,end="")
f.close()
print()
print(type(f))# <class '_io.TextIOWrapper'>
