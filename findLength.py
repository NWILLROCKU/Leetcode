class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        longest = 0
        
        while n >= 1 and n > longest:
            m = len(nums1) - n   # 0, 1, 2...
            for start_i in range(m + 1):
                #print('a:')
                #print(nums1[start_i : start_i + n])
                if start_i < m:
                    start_j = m
                else:
                    start_j = 0
                
                while start_j <= m:
                    #print('b:')
                    #print(nums2[start_j : start_j + n])
                    i = 0
                    while i < n:
                        if nums1[start_i + i]==nums2[start_j + i]:
                            i += 1
                        else:
                            break
                    longest = max(longest, i)
                    start_j += 1
            n -= 1
        return longest
