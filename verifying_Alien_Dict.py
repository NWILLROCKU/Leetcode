class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i=1
        while i < len(words):
            word1 = words[i-1]
            word2 = words[i]
            n = min(len(word1), len(word2))
            j = 0
            while j<n:
                k1 = order.index(word1[j])
                k2 = order.index(word2[j])
                if k1 < k2:
                    break
                elif k1 > k2:
                    return False
                j += 1
            if j==n and len(word1) > len(word2):
                return False
            i += 1
        return True
