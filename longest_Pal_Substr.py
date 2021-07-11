class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = s[0]
        n = len(s)
        evenCtr = [a-0.5 for a in range(1, n)] # even centers
        oddCtr = [a for a in range(1, n-1)]
        
        evenRad = -0.5
        oddRad = 0
        while len(evenCtr) > 0 or len(oddCtr) > 0:
            evenRad += 1
            oddRad += 1
            
            updatedLongest = False
            if evenCtr != [] and evenCtr[0] - evenRad < 0:
                evenCtr.pop(0)
            if evenCtr != [] and evenCtr[-1] + evenRad > n-1:
                evenCtr.pop()
            for i in range(len(evenCtr)):
                if s[evenCtr[i]-evenRad]==s[evenCtr[i]+evenRad]:
                    if updatedLongest==False:
                        longestPal = s[evenCtr[i]-evenRad : evenCtr[i]+evenRad+1]
                        updatedLongest = True
                else:
                    evenCtr.pop(i)
            
            updatedLongest = False
            if oddCtr != [] and oddCtr[0] - oddRad < 0:
                oddCtr.pop(0)
            if oddCtr != [] and oddCtr[-1] + oddRad > n-1:
                oddCtr.pop()
            for i in range(len(oddCtr)):
                if s[oddCtr[i]-oddRad]==s[oddCtr[i]+oddRad]:
                    if updatedLongest==False:
                        longestPal = s[oddCtr[i]-oddRad : oddCtr[i]+oddRad+1]
                        updatedLongest = True
                else:
                    oddCtr.pop(i)

        return longestPal
