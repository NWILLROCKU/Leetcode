        if s=='':
            return 0
        charList = s[0]
        maxCnt = 1
        i = 1
        n = len(s)
        while i < n:
            if s[i] in charList:
                maxCnt = max(len(charList), maxCnt)
                
                # Go to prev occurence of s[i]
                h = i-1
                while s[i-1] != offendingChar:
                    i -= 1
                charList = s[i]
            else:
                charList += s[i]
                if i==n-1:
                    maxCnt = max(len(charList), maxCnt)
            i += 1
        return maxCnt
