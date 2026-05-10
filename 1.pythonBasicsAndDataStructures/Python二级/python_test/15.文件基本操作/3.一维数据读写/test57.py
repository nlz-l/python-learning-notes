f = open("city.csv","r")
info = f.read()
f.close()
ls = info.split(",")#“，”拆分 返回列表
print(ls)
