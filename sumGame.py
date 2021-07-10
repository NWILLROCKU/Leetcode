class Solution:
    def sumGame(self, num: str) -> bool:
        sum1 = sum2 = 0
        n1 = n2 = 0
        n = len(num)
        for i in range(int(n/2)):
            if num[i]=='?':
                n1 += 1
            else:
                sum1 += int(num[i])
                
        for i in range(int(n/2), n):
            if num[i]=='?':
                n2 += 1
            else:
                sum2 += int(num[i])
                
                
        if (n1 + n2) % 2 != 0: # odd
            # Alice wins
            return True
        
        if (sum1 - sum2) == 4.5*(n2 - n1):
            return False
        return True
