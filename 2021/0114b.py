nums=[3,2,20,1,1,3]
x=10
arrSum = sum(nums)
target = arrSum - x
n = len(nums)
exitFlag= 0
for noRem in range(1,n+1):
    subArrSum = sum(nums[0:n-noRem])
    
    for starting_i in range(noRem+1):
        if starting_i > 0:
            subArrSum -= nums[starting_i]
            subArrSum += nums[n-1-noRem + starting_i]
        if subArrSum==target:
            exitFlag=1
            break
    if exitFlag==1:
        break
