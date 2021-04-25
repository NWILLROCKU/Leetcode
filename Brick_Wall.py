class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        cutLoc=[]
        for row in wall:
            if len(row) > 1:
                cutLoc.append([row[0]])
            else:
                cutLoc.append([])
            for j in range(1, len(row)-1):
                cutLoc[-1].append(cutLoc[-1][-1] + row[j])
        
        n = len(wall) # n = wall height
        minBricks = n
        cutLocs = []
        for i in range(n):
            if i==minBricks:
                return minBricks
            
            for x_cut in cutLoc[i]:
                if x_cut in cutLocs:
                    continue
                    
                cutLocs.append(x_cut)
                numBricks = n
                for i1 in range(i, n):
                    if x_cut in cutLoc[i1]:
                        numBricks -= 1
                
                if numBricks==0:
                    return 0
                minBricks = min(minBricks, numBricks)
        return minBricks
