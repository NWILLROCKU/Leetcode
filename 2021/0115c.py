        numList = []
        numCnt = []
        for num in nums:
            if num > k-1:
                continue

            if num in numList:
                i = numList.index(num)
                numCnt[i] += 1
            else:
                numList.append(num)
                numCnt.append(1)

        pairCnt = 0
        if k % 2 == 0:
            if k/2 in numList:
                i = numList.index(k/2)
                pairCnt += int(numCnt[i]/2)
                numList.pop(i)
                numCnt.pop(i)


        i = 0
        while i < len(numList):
            a = numList[i]
            b = k-a
            if b in numList:
                j = i+1+numList[i+1:].index(b)
                pairCnt += min(numCnt[i], numCnt[j])
                numList.pop(j)
                numCnt.pop(j)
            i += 1
        
        return pairCnt
