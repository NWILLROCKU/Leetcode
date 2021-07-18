class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        # maze2 = m x n array of -1's
        maze2 = []
        for i in range(m):
            maze2.append([-1]*n)
        
        def takeStep(i, j, m, n):
            if (i >= 0 and j >= 0 and i < m and j < n) and maze2[i][j]==-1: # within maze bounds, not yet encountered
                maze2[i][j] = 0 
                if maze[i][j]=='.': # open
                    coordList.append((i,j))
            
        
        stepCnt = 0
        i = entrance[0]
        j = entrance[1]
        coordList = [(i,j)]
        maze2[i][j] = 0
        while coordList != []:
            #print(coordList)
            #print(maze2)
            oldCoordList = coordList.copy()
            coordList = []
            for coordPair in oldCoordList:
                i = coordPair[0]
                j = coordPair[1]
                if stepCnt > 0 and (i in [0, m-1] or j in [0, n-1]):
                    return stepCnt
                takeStep(i+1, j, m, n)
                takeStep(i-1, j, m, n)
                takeStep(i, j+1, m, n)
                takeStep(i, j-1, m, n)
            stepCnt += 1
        return -1
        
                
