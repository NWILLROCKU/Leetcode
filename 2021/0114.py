n = len(nums)

leftCnt = 0
leftSum = 0
while leftCnt < len(nums) and leftSum < x:
    leftCnt += 1
    leftSum += nums[leftCnt]
# Now, leftCnt = len(nums) or leftSum >= x, or both
if leftCnt==len(nums):
    if leftSum != x:
        return -1
    return len(nums)
leftList = nums[0: leftCnt]

rightCnt = 0
rightSum = 0
while rightCnt < len(nums) and rightCnt < x:
    rightCnt += 1
    rightSum += nums[n-1-rightCnt]
rightList = nums[n-rightCnt :n]

class treeNode:
    def __init__(self, val=0):
        self.val = val
        self.left=None
        self.right=None

root = treeNode(0)
for i in leftList

    
