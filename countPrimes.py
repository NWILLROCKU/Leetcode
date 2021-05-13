class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        
        def isPrime(n):
            for i in range(3, int(math.sqrt(n))+1, 2): # n is odd, therefore it cannot be divisble by even numbers
                if n%i==0:
                    return False
            return True
        
        if n <= 2:
            return 0
        pCnt = 1
        for i in range(3, n, 2): # if >2, must be odd to be prime
            if i > 5 and (i%3==0 or i%5==0):
                continue
            if isPrime(i):
                pCnt += 1
        return pCnt
