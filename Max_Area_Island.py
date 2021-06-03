class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for row in grid:
            print(row)
            
        def updateID():
            data_i = activeID.index(grid[i][j])
            cnt[data_i] += 1
            updated[data_i] = True
            
        def addID():
            activeID.append(grid[i][j])
            cnt.append(1)
            updated.append(True)
            
        maxArea = 0
        m = len(grid)
        n = len(grid[0])
        if m==1 and n==1:
            return grid[0][0]
        nextID = 1
        
        activeID = []
        cnt = []
        for i in range(m):
            updated = [False]*len(activeID)
            for j in range(n):
                # Don't do anything if value is 0
                if grid[i][j]==0:
                    continue
                
                # First row
                if i==0: 
                    if j > 0 and grid[i][j-1] > 0: # same as left
                        grid[i][j] = grid[i][j-1]
                        updateID()
                    else:
                        grid[i][j] = nextID
                        nextID += 1
                        addID()     
                        
                else:
                    if grid[i-1][j] > 0: # Check row above
                        grid[i][j] = grid[i-1][j]
                        updateID()
                        if j > 0 and grid[i][j-1] > 0: # Check prev column, if 2nd or greater column
                            # Merge the two IDs to grid[i][j-1]
                            if grid[i][j-1] != grid[i-1][j]:
                                grid[i][j] = grid[i][j-1]
                                dataL = activeID.index(grid[i][j-1])
                                dataU = activeID.index(grid[i-1][j])
                                
                                cnt[dataL] += cnt[dataU]
                                cnt.pop(dataU)
                                activeID.pop(dataU)
                                if dataU < dataL:
                                    updated[dataL-1] = updated.pop(dataU)
                                else:
                                    updated[dataL] = updated.pop(dataU)
                                
                    elif j > 0 and grid[i][j-1] > 0: # Check prev column, if 2nd or greater column
                        grid[i][j] = grid[i][j-1]
                        updateID()
                    else:
                        grid[i][j] = nextID
                        nextID += 1
                        addID()
            # Trim entries that haven't been updated this row
            data_i = 0
            while data_i < len(cnt):
                if not updated[data_i] or i==m-1:
                    maxArea = max(maxArea, cnt.pop(data_i))
                    activeID.pop(data_i)
                    updated.pop(data_i)
                else:
                    data_i += 1
                    
        print('New grid: ')
        for row in grid:
            print(row)
        return maxArea
