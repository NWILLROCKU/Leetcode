class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        
        if n <= 2:
            return 0
        pList = [2]
        for i in range(3,n):
            j = 0
            root = math.sqrt(i)
            for j in range(len(pList)):
                if pList[j] > root:
                    pList.append(i)
                    break
                if i % pList[j]==0:
                    break
                
        return len(pList)
