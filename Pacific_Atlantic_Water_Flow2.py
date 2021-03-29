class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        h = matrix
        m = len(h)
        n = len(h[0])
        
        pac = []
        for i in range(m):
            pac.append([0]*n)
            for j in range(n):
                if i==0 or j==0 or h[i-1][j] <= h[i][j] or h[i][j-1] <= h[i][j]:
                    pac[i][j] = 1
            
        
        coordL = []
        i = 0
        j = 0
        for i in range(m):
            for j in range(n):
                pacFlag = 0 # flag that water will run into the pacific ocean
                val = arr[i][j]
                
                # Check westward flow
                j2 = 0
                while j2 < j:
                    if i==1 and j==4:
                        print(j2)
                    if arr[i][j2] > arr[i][j2+1]:
                        break
                    j2 += 1
                if i==1 and j==4:
                    print(j2)
                if j2==j:
                    pacFlag = 1

                # Check northward flow if there is no westward flow
                if pacFlag==0:
                    i2 = 0
                    while i2 < i:
                        if arr[i2][j] > arr[i2+1][j]:
                            break
                        i2 += 1
                    if i2==i:
                        pacFlag = 1
                
                # Check Atlantic flow if there is Pacific flow
                if pacFlag==1:
                    # Check eastward flow
                    j2 = n-1
                    while j2 > j:
                        if arr[i][j2] > arr[i][j2-1]:
                            break
                        j2 -= 1
                    if j2==j:
                        coordL.append([i,j])
                    else:
                        # Check southward flow
                        i2 = m-1
                        while i2 > i:
                            if arr[i2][j] > arr[i2-1][j]:
                                break
                            i2 -= 1
                        if i2==i:
                            coordL.append([i,j])
        return coordL
                    
