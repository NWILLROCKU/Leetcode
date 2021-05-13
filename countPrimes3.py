class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        
        if n <= 2:
            return 0
        prime = [1]*n
        prime[0] = prime[1] = 0
        i = 2
        while i <= sqrt(n-1):
            if prime[i]==1:
                for j in range(i**2, n, i):
                    prime[j] = 0
            i += 1
        return sum(prime)
