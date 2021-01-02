numbers = [-7,9,5,2,1,7,-1,0,-2]

triplets=[]
for i in range(len(numbers)):
    num1 = numbers[i]
    i2 = i + 1
    while i2 < len(numbers):
        num2 = numbers[i2]
        i3 = i2 + 1
        while i3 < len(numbers):
            if num1 + numbers[i2] + numbers[i3] == 0:
                skipFlag = 0
                if len(triplets) > 0:
                    # Check if a duplicate triplet
                    for t in range(len(triplets)):
                        myTrip = list(triplets[t])
                        if num1==triplets[t][0] or num1==triplets[t][1] or num1==triplets[t][2]:
                            myTrip.remove(num1)
                            if num2==myTrip[0] or num2==myTrip[1]:
                                myTrip.remove(num2)
                                if numbers[i3]==myTrip[0]:
                                    skipFlag = 1
                                    break
                if skipFlag == 0:
                    triplets.append([num1, numbers[i2], numbers[i3]])
                    break
            i3 += 1
        i2 += 1
print(triplets)
