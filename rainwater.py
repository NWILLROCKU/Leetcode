height = [0,1,0,2,1,0,1,3,2,1,2,1]

heightList = list(set(height))
heightList.sort()
heightList.reverse()

water = 0
n = len(height)
i = 1
while i < n:
    if height[i] < height[i-1]:
        peak1 = i-1
        print("Peak 1: " + str(peak1))
        break
    i += 1        

while i < n:
    # Next peak not found
    if height[i] < height[peak1]:
        i += 1
        continue
        
    peak2 = i
    print("Peak 2: " + str(peak2))

    # Add water
    waterLvl = min(height[peak1], height[peak2])
    for i in range(peak1 + 1, peak2):
        water += waterLvl - height[i]

    peak1 = peak2
    print("Peak 1: " + str(peak1))
    i = peak1+1

