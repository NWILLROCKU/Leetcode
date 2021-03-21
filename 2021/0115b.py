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
    if k-a in numList:
        i = numList.index(a)
        j = numList.index(k-a)
        pairCnt += min(numCnt[i], numCnt[j])
