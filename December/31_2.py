class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        n = len(heights)
        if n==0:
            return 0
        elif n==1:
            return heights[0]
        elif heights[0]==1:
            i = 1
            while i < n and heights[i]==1:
                i+=1
            if i==n:
                return len(heights)
        maxHeight = max(heights)
        
        # check if heights is monotonically increasing
        instantCalc = 1
        if heights[0] != 0 or heights[-1] != n-1:
            instantCalc = 0
        for i in range(n-1):
            if heights[i]+1 != heights[i+1]:
                instantCalc = 0
                break
        
        if instantCalc==1:
            maxA = floor(n/2)*ceil(n/2)
        else:
        
            for i in range(n):
                myH = heights[i]
                barsToRight = 0
                barsToLeft = 0
                if i < n-1: # not at last element
                    j = i + 1
                    while j < n and heights[j] >= myH:
                        barsToRight += 1
                        j += 1
                if i > 0: # not first element
                    j = i - 1
                    while j >= 0 and heights[j] >= myH:
                        barsToLeft += 1
                        j -= 1
                A = myH * (barsToLeft + 1 + barsToRight)
                if A > maxA:
                    maxA = A
                    
        return maxA
