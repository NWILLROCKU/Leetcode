class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def placeQ(r0, c0, nqueens, n):
            nqueens += 1
            qCoords.append([r0, c0])
            
            if nqueens==n:
                qCoords.sort()
                print('qClist before: ', qClist)
                print('qCoords: ', qCoords)
                if qCoords not in qClist:
                    qClist.append(qCoords.copy())
                print('qClist after: ', qClist)
                print()
            else:
                # Block out spaces

                for r in range(n):
                    board[r][c0] = 0
                for c in range(n):
                    board[r0][c] = 0

                # \
                r, c = r0, c0
                while r >= 0 and c >= 0:
                    board[r][c] = 0
                    r -= 1
                    c -= 1
                r, c = r0, c0
                while r < n and c < n:
                    board[r][c] = 0
                    r += 1
                    c += 1

                # /
                r, c = r0, c0
                while r >= 0 and c < n:
                    board[r][c] = 0
                    r -= 1
                    c += 1
                r, c = r0, c0
                while r < n and c >= 0:
                    board[r][c] = 0
                    r += 1
                    c -= 1

                for r, row in enumerate(board):
                    for c, val in enumerate(row):
                        if val: # 0 = blocked, 1 = not blocked
                            placeQ(r, c, nqueens, n)
        
        qClist = []
        for r in range(n):
            for c in range(n):
                # Empty queen coordinate list
                qCoords = []
                
                # Reset board
                board = []
                for i in range(n):
                    board.append([1]*n)
                
                placeQ(r, c, 0, n)
        
        # Convert to solution format
        sols = []
        for qCoords in qClist:
            sol = []
            i = 0
            for r in range(n):
                rowstr = ''
                for c in range(n):
                    if i < len(qCoords) and r==qCoords[i][0] and c==qCoords[i][1]:
                        i += 1
                        rowstr += 'Q'
                    else:
                        rowstr += '.'
                sol.append(rowstr)
            sols.append(sol)
        return sols
