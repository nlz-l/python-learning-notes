#字典函数方法

# d.keys() d.values() d.items() d.get(key,default) d.pop(key,default)
# d.popitem() d.clear()

d = {"2001101":"刘备","2001102":"关羽","2001103":"张飞","2001104":"赵云"}

#d.key() 返回所有键的信息

print(d.keys())
print(type(d.keys()))# <class 'dict_keys'>

#d.values() 返回所有的值的信息

print(d.values())
print(type(d.values()))# <class 'dict_values'>

#d.items() 返回所有的键值对

print(d.items())
print(type(d.items()))# <class 'dict_items'>

#d.get(key,default) 键存在则返回相应值，否则返回默认值default

print(d.get("2001101"))
print(d.get("2001106","查无此人")) #默认default
# print(d[1001106]) 报错

#d.pop(key,default) 键存在则删除相应键值对，并返回相应值，否则返回default
#不可空
d.pop("2001101")
print(d)
d[2001101] = "刘备"
print(d)
#d.popitem() 随机从字典中取出一个键值对，以元组(key,value)形式返回，
#同时将该键值对从字典中删除
print(d.popitem())
print(d)

#d.clear() 清空字典 d 中所有键值对
d.clear()
print(d) # {}s
