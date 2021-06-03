class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        
        maxProd = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                prod = len(words[i]) * len(words[j])
                if prod <= maxProd:
                    break
                ltr_i = 0
                while ltr_i < len(words[j]):
                    ltr = words[j][ltr_i]
                    if ltr in words[i]:
                        break
                    ltr_i += 1
                if ltr_i==len(words[j]):
                    maxProd = prod
        return maxProd
                        
