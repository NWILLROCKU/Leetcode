class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        uni = []
        cnt = []
        for i in range(len(nums)-1, -1, -1):
            j = 0
            while j < len(uni):
                if uni[j] >= nums[i]:
                    if uni[j] == nums[i]:
                        cnt[j] += 1
                    else:
                        uni.insert(j, nums[i])
                        cnt.insert(j, 1)
                    
                    break
                j += 1
            if j==len(uni):
                uni.append(nums[i])
                cnt.append(1)
            nums[i] = sum(cnt[:j])
            #print(uni)
            #print(cnt)
        return nums
