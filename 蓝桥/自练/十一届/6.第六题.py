n = int(input())
a_num = 0
b_num = 0
for i in range(n):
  score = int(input())
  if score >= 60:
    a_num += 1
  if score >= 85:
    b_num += 1
a_num = round((a_num/n)*100)
b_num = round((b_num/n)*100)
print(f'{a_num}%')
print(f'{b_num}%')