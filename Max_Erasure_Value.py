class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        a = 0
        for b in range(1, len(nums)+1):
            subArr = nums[a:b]
            maxSum = max(maxSum, sum(subArr))
            if b < len(nums) and nums[b] in subArr:
                offset = subArr.index(nums[b])
                a += offset + 1
        return maxSum
