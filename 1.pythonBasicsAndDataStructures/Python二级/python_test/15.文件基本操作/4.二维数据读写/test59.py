f = open("students.csv","r")
ls = []
for line in f:
    line.strip("\n")
    temp = line.split(",")
    ls.append(temp)
f.close()
print(ls)
