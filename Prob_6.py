numbers = [-7,9,5,2,1,7,-1]

twins=[]
skipFlag = 0
for i in range(len(numbers)):
    num1 = numbers[i]
    for t in range(len(twins)):
        if num1==twins[0] or num1==twins[1]:
            skipFlag = 1
            break
    if skipFlag==1:
        skipFlag = 0
        continue
    i2 = i + 1
    while i2 < len(numbers):
        if num1 + numbers[i2] == 0:
            twins.append([num1, numbers[i2]])
            break
