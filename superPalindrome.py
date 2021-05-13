class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        import math as m
        root1 = m.ceil(m.sqrt(int(left)))
        root2 = m.floor(m.sqrt(int(right)))
        palCnt = 0 # number of super-palindromes
        for i in range(root1, root2+1):
            i_str = str(i)
            if i_str==i_str[::-1]:
                i2_str = str(i**2)
                if i2_str==i2_str[::-1]:
                    palCnt += 1
        return palCnt
