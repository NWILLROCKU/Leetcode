class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def getMax(k, maxSum, mysum):
            if mysum <= k:
                if isinstance(maxSum, int):
                    #print('maxSum is int')
                    return max(mysum, maxSum)
                else:
                    #print('hi')
                    return mysum
            else:
                return maxSum
        
        m = len(matrix) # >=1
        n = len(matrix[0]) # <=100
        
        # Build sumarr
        for row in matrix:
            for j in range(1, len(row)):
                row[j] += row[j-1]
        
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += matrix[i-1][j]
        
        #print(matrix)
        maxSum = None
        for i1 in range(-1, m-1):
            for j1 in range(-1, n-1):
                
                for i2 in range(i1+1, m):
                    for j2 in range(j1+1, n):
                        mysum = matrix[i2][j2]
                        
                        if i1 == -1:
                            if j1 != -1:
                                mysum -= matrix[i2][j1]
                                
                        else: # i1 >= 0
                            if j1 ==-1:
                                mysum -= matrix[i1][j2]
                            else:
                                mysum -= matrix[i1][j2] + matrix[i2][j1] - matrix[i1][j1]
                        maxSum = getMax(k, maxSum, mysum)
        return maxSum
