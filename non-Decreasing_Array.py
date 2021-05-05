class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def check2(nums):
            i = 1
            while i < len(nums):
                if nums[i-1] > nums[i]:
                    break
                i += 1
            return i
        
        i = check2(nums)
        print(i)
        if i==len(nums):
            return True
        
        nums_orig = nums.copy()
        i_orig = i
        
        nums.pop(i)
        if check2(nums)==len(nums):
            return True
        
        nums_orig.pop(i_orig - 1)
        if check2(nums_orig)==len(nums_orig):
            return True
        
        return False
                
