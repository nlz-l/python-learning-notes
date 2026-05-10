#输入一个成绩，判断这个成绩是及格？优秀？不及格？

score = float(input("请输入你的成绩："))

if score >=60:
    if score < 80:
        print("普通及格")
    else:
        print("优秀")
else:
    print("不及格")
