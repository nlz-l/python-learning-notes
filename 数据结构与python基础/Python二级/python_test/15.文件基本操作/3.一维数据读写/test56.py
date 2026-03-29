path = "C:\\Users\\liuwenbo\\Desktop\\文件夹\\python_test\\15.文件基本操作\\3.一维数据读写\\test"

ls = ['北京','上海','深圳','广州']
f =open("city.csv","w")
s = ",".join(ls)
f.write(s)
f.close()
