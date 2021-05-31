nums = [0,0,1]

zerosRemoved = 0
for i in nums:
    if i==0:
        nums.remove(0)
        zerosRemoved += 1
for i in range(zerosRemoved):
    nums.append(0)
