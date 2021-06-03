class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)

        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        
        ymax = 0
        for i in range(1, len(horizontalCuts)):
            ymax = max(ymax, horizontalCuts[i] - horizontalCuts[i-1])

        xmax = 0
        for i in range(1, len(verticalCuts)):
            xmax = max(xmax, verticalCuts[i] - verticalCuts[i-1])
        
        return int((xmax*ymax) % (1e9 + 7))
