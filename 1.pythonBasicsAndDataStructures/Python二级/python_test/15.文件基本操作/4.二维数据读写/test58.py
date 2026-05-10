students = [
            ["学号","姓名","性别","年龄"],
            ["1001","张三","男","20"],
            ["1002","张四","女","21"],
            ["1003","张五","男","23"],
            ["1004","张六","男","21"]
            ]

print(students[1])
print(students[1][2])
for s in students:
    for i in s:
        print(i)

f = open("students.csv","w")
for row in students:
    f.write(",".join(row) + "\n")
f.close()
