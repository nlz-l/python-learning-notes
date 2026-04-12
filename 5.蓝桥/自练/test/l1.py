import os
import sys

count = 0
a = ''
for i in range(1, 2027):
    a+=str(i)
    b = int(a)
    if b % 26 == 0:
        count += 1
print(count)