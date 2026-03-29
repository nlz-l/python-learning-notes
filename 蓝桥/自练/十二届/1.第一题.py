num = int(input())
n = 0
ans = 0
count = 0
while num > 0:
  ans += 1
  num -= ans
  count += 1
print(count)