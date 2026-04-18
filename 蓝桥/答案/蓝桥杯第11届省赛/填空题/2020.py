nums=[["2","2","0","0","0","0"],
      ["0","0","0","0","0","0"],
      ["0","0","2","2","0","2"],
      ["0","0","0","0","0","0"],
      ["0","0","0","0","2","2"],
      ["0","0","2","0","2","0"]]
count=0
# 每行遍历
for i in range(len(nums)):
    for j in range(len(nums)-3):
        if nums[i][j]=='2' and nums[i][j+1]=='0' and nums[i][j+2]=='2' and nums[i][j+3]=='0':
            count+=1
# 每列遍历
for i in range(len(nums)):
    for j in range(len(nums)-3):
        if nums[j][i]=='2' and nums[j+1][i]=='0' and nums[j+2][i]=='2' and nums[j+3][i]=='0':
            count+=1
# 每斜行遍历
for i in range(len(nums)-3):
    for j in range(len(nums)-3):
        if nums[i][j]=='2' and nums[i+1][j+1]=='0' and nums[i+2][j+2]=='2' and nums[i+3][j+3]=='0':
            count+=1
print(count)#5