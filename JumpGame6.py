class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dist = 1
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                dist = 1
            else:
                dist += 1
            
            if dist > k:
                nums[i] += max(nums[i-k:i])
        return nums[-1]
