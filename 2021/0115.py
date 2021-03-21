unpaired = []
unpairedCnt = []
pairCnt = 0
for num in nums:
    if num in otherHalf: # could replace w try
        i = otherHalf.index(num)
        otherHalf.pop(i)
        pairCnt += 1
        if unpairedCnt[i] > 1:
            unpairedCnt[i] -= 1
        else:
            unpaired.pop(i)
            unpairedCnt.pop(i)
    else:
        if num in unpaired:
            i = unpaired.index(num)
            unpairedCnt[i] += 1
        else:
            unpaired.append(num)
            unpairedCnt.append(1)
            otherHalf.append(k-num)
return pairCnt
