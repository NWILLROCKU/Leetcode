<<<<<<< HEAD
=======
# This uses the "Expand around center" method
>>>>>>> a80a1466e6773868e1eb4096f8d4df61ce747541
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
<<<<<<< HEAD
            for i in range(len(evenCtr)):
                if s[evenCtr[i]-evenRad]==s[evenCtr[i]+evenRad]:
                    if updatedLongest==False:
                        longestPal = s[evenCtr[i]-evenRad : evenCtr[i]+evenRad+1]
                        updatedLongest = True
=======
            i = 0
            while i < len(evenCtr):
                even1 = int(evenCtr[i]-evenRad)
                even2 = int(evenCtr[i]+evenRad)
                if s[even1]==s[even2]:
                    if updatedLongest==False:
                        longestPal = s[even1:even2+1]
                        updatedLongest = True
                    i += 1
>>>>>>> a80a1466e6773868e1eb4096f8d4df61ce747541
                else:
                    evenCtr.pop(i)
            
            updatedLongest = False
            if oddCtr != [] and oddCtr[0] - oddRad < 0:
                oddCtr.pop(0)
            if oddCtr != [] and oddCtr[-1] + oddRad > n-1:
                oddCtr.pop()
<<<<<<< HEAD
            for i in range(len(oddCtr)):
=======
            i = 0
            while i < len(oddCtr):
>>>>>>> a80a1466e6773868e1eb4096f8d4df61ce747541
                if s[oddCtr[i]-oddRad]==s[oddCtr[i]+oddRad]:
                    if updatedLongest==False:
                        longestPal = s[oddCtr[i]-oddRad : oddCtr[i]+oddRad+1]
                        updatedLongest = True
<<<<<<< HEAD
=======
                    i += 1
>>>>>>> a80a1466e6773868e1eb4096f8d4df61ce747541
                else:
                    oddCtr.pop(i)

        return longestPal
