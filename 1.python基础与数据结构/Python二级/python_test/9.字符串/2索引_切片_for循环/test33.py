#索引 0 到 n-1

s = "How are you doing?"
print(s[0])# H
print(s[17])# ?
print(s[-1])#?

#切片 [开始索引:结束索引:步长]  
'''左闭右开'''

print(s[1:6])# ow ar
print(s[1:])# ow are you doing?
print(s[:8])# How are
print(s[0:8])# How are
print(s[:])# How are you doing?


#步长

print(s[0:11])# How are you
print(s[0:11:1])# How are you
print(s[0:11:2])# Hwaeyu
print(s[::-1])# ?gniod uoy era woH  逆序排列


