        posList = []
        i = 0
        while i < len(s):
            if s[i]==c:
                posList.append(i)
            i += 1
        
        dist = [0]*len(s)
        i = 0
        pos1 = posList[0]
        while i <= pos1:
            dist[i] = pos1 - i
            i += 1
        if len(posList)==1:
            while i < len(s):
                dist[i] = i - pos1
                i += 1
            return dist
        
        for j in range(1, len(posList)):
            pos0 = pos1
            pos1 = posList[j]
            for i in range(pos0 + 1, pos1 + 1):
                dist[i] = min(i - pos0, pos1 - i)
        
        for i in range(pos1 + 1, len(s)):
            dist[i] = i - pos1
        return dist
