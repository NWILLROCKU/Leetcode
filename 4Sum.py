nums= [1,0,-1,0,-2,2]
target  =0

digit = []
appCnt = []
for i in nums:
    if i not in digit:
        digit.append(i)
        appCnt.append(nums.count(i))

n = len(digit)
pairsum = []
for d1 in digit:
    pairsum.append([])
    for d2 in digit:
        if len(pairsum)==0:
            pairsum = [[d1+d2]]
        elif len(pairsum[-1])==0:
            pairsum[-1] = [d1+d2]
        else:
            pairsum[-1].append(d1+d2)

numlist = []
skipFlag = 0
for i in range(n):
    appCnt[i] -= 1
    for j in range(n):
        if appCnt[j]==0:
            continue
        appCnt[j] -= 1

        for i2 in range(n):
            if appCnt[i2]==0:
                continue
            appCnt[i2] -= 1
            for z in numlist:
                if digit[i] in z and digit[j] in z and digit[i2] in z:
                    skipFlag = 1
                    break
            if skipFlag==1:
                skipFlag = 0
                continue

            for j2 in range(n):
                if pairsum[i][j] + pairsum[i2][j2] != target:
                    continue
                if appCnt[j2]==0:
                    continue
                
                if len(numlist)==0:
                    numlist = [[digit[i], digit[j], digit[i2], digit[j2]]]
                numlist.append([digit[i], digit[j], digit[i2], digit[j2]])
                break
            appCnt[i2] += 1
        appCnt[j] += 1
    appCnt[i] += 1
