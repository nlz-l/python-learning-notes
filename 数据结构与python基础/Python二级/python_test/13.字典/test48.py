# {<键1>:<值1>,<键2>:<值2>,...,<键n>:<值n>}
#字典无序

d = {"2001101":"刘备","2001102":"关羽","2001103":"张飞","2001104":"赵云"}
print(d)
print(type(d))#<class 'dict'>

#字典索引

print(d["2001102"])

# print(d["2001106"]) 报错

d["2001102"] = "马超"
print(d)

d["2001105"] = "张辽"
print(d)

# len(d) min(d) max(d)

print(len(d))
print(min(d))
print(max(d))


#看key
print("2001101" in d)
print("刘备" not in d)
