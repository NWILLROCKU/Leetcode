class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums = list(set(nums))
        nums.sort()
        maxCons = 0
        consLen = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1] + 1:
                consLen += 1
            else:
                maxCons = max(maxCons, consLen)
                consLen = 1
        maxCons = max(maxCons, consLen)
        return maxCons
