ls = ['2','0','5']
ans = 0
for i in range(2025,20250413):
  ls1 = list(str(i))
  count = 0
  for j in ls1:
    if int(j) == 2:
        count += 1
  if count >= 2 and ls[1] in ls1 and ls[2] in ls1:
    ans += 1
print(ans)