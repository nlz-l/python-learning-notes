strs = input()
a = 0
b = []
for i in strs:
  c = strs.count(i)
  if c>a:
    a = c
for i in strs:
  if strs.count(i) == a:
    b.append(i)
b.sort()
print(b[0])
print(a)
