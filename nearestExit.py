class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        maze2 = []
        for i in range(m):
            maze2.append([-1]*n)
        
        def takeStep(i, j, stepCnt, m, n):
            if i >= 0 and j >= 0 and i < m and j < n: # within maze bounds
                if (maze2[i][j]==-1 or maze2[i][j] > stepCnt) and maze[i][j]=='.': # open, not yet encountered
                    maze2[i][j] = stepCnt # no. of steps it takes to reach that square
                    #print(maze2)
            
                    takeStep(i+1, j, stepCnt+1, m, n)
                    takeStep(i-1, j, stepCnt+1, m, n)
                    takeStep(i, j+1, stepCnt+1, m, n)
                    takeStep(i, j-1, stepCnt+1, m, n)
        
        takeStep(entrance[0], entrance[1], 0, m, n)
        #print(maze2)
        minSteps = []
        for j in maze2[0]:
            if j > 0:
                minSteps.append(j)
        for j in maze2[-1]:
            if j > 0:
                minSteps.append(j)
        for i in maze2:
            if i[0] > 0:
                minSteps.append(i[0])
            if i[-1] > 0:
                minSteps.append(i[-1])
        if minSteps==[]:
            return -1
        return min(minSteps)
                
