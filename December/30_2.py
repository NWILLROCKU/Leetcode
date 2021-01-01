class Solution(object):
    def gameOfLife(self, board):
        def getNeighbors(i, j, b, prevRow, leftCell):
            m = len(b)
            n = len(b[0])
            if i==0:
                if j==0: # top left corner
                    if m==1:
                        return [b[i][j+1]]
                    elif n==1:
                        return [b[i+1][j]]
                    else:
                        return [b[i+1][j], b[i+1][j+1], b[i][j+1]]
                elif j==n-1: # top right corner
                    if m==1:
                        return [leftCell]
                    else:
                        return [b[i+1][j], b[i+1][j-1], leftCell]
                else: # top row
                    if m==1:
                        return [leftCell, b[i][j+1]]
                    else:
                        return [b[i+1][j], b[i+1][j-1], b[i+1][j+1], leftCell, b[i][j+1]]
            elif i==m-1:
                if j==0: # bottom left corner
                    if n==1:
                        return [prevRow[j]]
                    else:
                        return [prevRow[j], prevRow[j+1], b[i][j+1]]
                elif j==n-1:
                    return [prevRow[j], prevRow[j-1], leftCell]
                else:
                    return [prevRow[j], prevRow[j-1], prevRow[j+1], leftCell, b[i][j+1]]
            elif j==0: # left col
                    if n==1:
                        return [b[i+1][j], prevRow[j]]
                    else:
                        return [b[i][j+1], b[i+1][j+1], prevRow[j+1], b[i+1][j], prevRow[j]]
            elif j==n-1:
                return [leftCell, b[i+1][j-1], prevRow[j-1], b[i+1][j], prevRow[j]]
            else:
                return [leftCell, b[i+1][j-1], prevRow[j-1], b[i+1][j], prevRow[j], b[i][j+1], b[i+1][j+1], prevRow[j+1]]

        prevCell = 0
        prevRow = []
        m = len(board)
        n = len(board[0])
        if m==1 and n==1:
            board[0][0] = 0
        else:        
            for i in range(m):
                curRow = list(board[i])
                for j in range(n):
                    neighbors = getNeighbors(i, j, board, prevRow, prevCell)
                    prevCell = board[i][j]
                    if board[i][j]==0:
                        if sum(neighbors)==3:
                            board[i][j] = 1
                    else:
                        if sum(neighbors) < 2 or sum(neighbors) > 3:
                            board[i][j] = 0
                prevRow = list(curRow)
        
