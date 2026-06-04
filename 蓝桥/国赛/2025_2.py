count = 1
ls = []
for i in range(1,2026):
  if i not in ls:
    ls.append(i)
    count += 1
    if i % 2 == 0 and i % 2 in ls:
      ls = ls[:-1]
      count -= 1
print(count)
