class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxLen = 0
        for i, dig1 in enumerate(nums1):
            cur_j = []
            curLen = []
            for j, dig2 in enumerate(nums2):
                if dig1==dig2:
                    cur_j.append(j)
                    if i > 0 and j > 0 and j-1 in prev_j:
                        curLen.append(prevLen[prev_j.index(j-1)] + 1)
                    else:
                        curLen.append(1)
            if curLen != []:
                maxLen = max(maxLen, max(curLen))
            prev_j = cur_j.copy()
            prevLen = curLen.copy()
        return maxLen
