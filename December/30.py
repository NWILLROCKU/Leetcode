#board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
def getNeighbors(i, j, b, prevRow, leftCell):
    m = len(b)
    n = len(b[0])
    if i==0:
        if j==0:
            return [b[i+1][j], b[i+1][j+1], b[i][j+1]]
        elif j==n-1:
            return [b[i+1][j], b[i+1][j-1], leftCell]
        else:
            return [b[i+1][j], b[i+1][j-1], b[i+1][j+1], leftCell, b[i][j+1]]
    elif i==m-1:
        if j==0:
            return [prevRow[j], prevRow[j+1], b[i][j+1]]
        elif j==n-1:
            return [prevRow[j], prevRow[j-1], leftCell]
        else:
            return [prevRow[j], prevRow[j-1], prevRow[j+1], leftCell, b[i][j+1]]
    elif j==0:
        return [b[i][j+1], b[i+1][j+1], prevRow[j+1], b[i+1][j], prevRow[j]]
    elif j==n-1:
        return [leftCell, b[i+1][j-1], prevRow[j-1], b[i+1][j], prevRow[j]]
    else:
        return [leftCell, b[i+1][j-1], prevRow[j-1], b[i+1][j], prevRow[j], b[i][j+1], b[i+1][j+1], prevRow[j+1]]

prevCell = 0
prevRow = []
m = len(board)
n = len(board[0])
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
print(board)
        
