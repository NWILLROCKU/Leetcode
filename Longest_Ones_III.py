class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        zCnt = 0 # zero count
        i1 = i2 = 0
        n = len(nums)
        
        # Initialize i2 & maxLen
        while zCnt < k and i2 < n:
            if nums[i2]==0:
                zCnt += 1
            i2 += 1
            while nums[i2]==1
        # Now, i2 = n or (index of kth zero) + 1, whichever comes sooner
        maxLen = max(maxLen, i2-i1)
        print(i1, i2, nums[i1:i2])
        
        while i2 < n:
            # Move i1 such that the subarray "poops" out a 0
            while i1 < n and nums[i1] != 0:
                i1 += 1
            # Now nums[i1] == 0 or i1==n
            i1 += 1
            
            # Move i2 after the next 0
            while i2 < n and nums[i2] != 0:
                i2 += 1
            # i2 at next 0
            i2 += 1
            
            print(i1, i2, nums[i1:i2])
            maxLen = max(maxLen, i2-i1)
        return maxLen
