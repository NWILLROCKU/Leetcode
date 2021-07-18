class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def appendString(ans, s, rowInd):
            for i in rowInd:
                if not s[i].isnumeric():
                    ans += s[i]
            return ans
        
        m = numRows
        n = len(s)
        if m==1 or n==1:
            return s
        
        ans = ''
        if (n-1) % (m-1) != 0:
            remainder = (n-1) % (m-1)
            for i in range(m-1-remainder):
                s += '1'
        n = len(s)
                
        # 1st row
        rowInd = [j for j in range(0, n, 2*(m-1))]
        ans = appendString(ans, s, rowInd)
            
        # 2nd row
        if m > 2:
            #print(rowInd)
            rowInd_prev = rowInd.copy()
            rowInd = [rowInd_prev[0] + 1]
            for j in range(1, len(rowInd_prev)):
                rowInd.append(rowInd_prev[j]-1)
                if j == len(rowInd_prev)-1 and rowInd_prev[j]==n-1:
                    break
                rowInd.append(rowInd_prev[j]+1)

            ans = appendString(ans, s, rowInd)
            #print(rowInd)
        
        # Middle rows
        for i in range(2, m-1):
            for j in range(len(rowInd)):
                if j % 2==0:
                    rowInd[j] += 1
                else:
                    rowInd[j] -= 1
                if rowInd[j]==len(s):
                    rowInd.pop()
            ans = appendString(ans, s, rowInd)
            #print(rowInd_prev, rowInd, ans)
            
        # Last row
        rowInd = [j for j in range(m-1, n, 2*(m-1))]
        ans = appendString(ans, s, rowInd)
            
        return ans
        
