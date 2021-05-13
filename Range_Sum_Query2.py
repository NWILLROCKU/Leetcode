class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        if n > m: # matrix is wider than it is tall
            for i in range(m):
                for j in range(1,n):
                    matrix[i][j] += matrix[i][j-1]
            self.sum_x = 1 # did sums in the x direction (along the row)
        else:
            for j in range(n):
                for i in range(1,m):
                    matrix[i][j] += matrix[i-1][j]
            self.sum_x = 0 # did sums in the y direction (along column)
        self.a = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mysum = 0
        if self.sum_x==1:
            for i in range(row1, row2+1):
                mysum += self.a[i][col2]
                if col1 > 0:
                    mysum -= self.a[i][col1-1]
        else:
            for j in range(col1, col2+1):
                mysum += self.a[row2][j]
                if row1 > 0:
                    mysum -= self.a[row1-1][j]
        return mysum
                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
