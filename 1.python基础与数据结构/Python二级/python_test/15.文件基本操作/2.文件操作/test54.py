#f.seek(offset)
#改变当前文件操作指针的位置，
#offset的值：0为文件开头；1为从当前位置开始；2为文件结尾
path1 = "C:/Users/liuwenbo/Desktop/文件夹/python_test/15.文件基本操作/2.文件操作/a/test.txt"
f1 = open(path1,"rt",encoding="UTF-8")
s1 = f1.read()
print(s1)
f1.seek(0)
ls = f1.readlines()
print(ls)
f1.close()

#写
#f.write(s) 向文件写入一个字符串或字节流
#f.writelines(lines) 将一个元素为字符串的列表整体写入文件

path2 = "C:/Users/liuwenbo/Desktop/文件夹/python_test/15.文件基本操作/2.文件操作/a/test2.txt"
f2 = open(path2,"w")#覆盖写
f2.write("1\n")
f2.write("2\n")
f2.write("3\n")
f2.close()

path3 = "C:/Users/liuwenbo/Desktop/文件夹/python_test/15.文件基本操作/2.文件操作/a/test3.txt"
f3 = open(path3,"a")#追加写
ls = ["1\n","2\n","3\n"]
f3.writelines(ls)
f3.close()
