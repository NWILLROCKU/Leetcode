class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0]*n for _ in range(m)]
        for i, dig1 in enumerate(nums1):
            for j, dig2 in enumerate(nums2):
                if dig1==dig2:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
        return max(max(row) for row in dp)
