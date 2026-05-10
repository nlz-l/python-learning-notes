# 中文在gbk 中占2个字节 utf-8 中占3个字节  其他 1个字节

s1 = '卧槽123abc!@#'

print(s1.encode())
print(s1.encode('utf-8'))
print(s1.encode('gbk'))

bys =b'\xe5\x8d\xa7\xe6\xa7\xbd123abc!@#'
print(type(bys))
s2 = bys.decode()
s3 = bys.decode('utf-8')
print(s2)
print(s3)

s4 = bys.decode('gbk')
print(s4)
