ls = [1,2,3,4]
nums = []
for a in ls:
    for b in ls:
        if a == b:
            continue
        for c in ls:
            if a == c or c ==b:
                continue
            nums.append(100*a+10*b+c)
print(f'共有{len(nums)}个')
print(nums)
