height = [4,2,0,3,2,5]

heightList = list(set(height))
heightList.sort()
heightList.reverse()

water = 0
n = len(height)
i = 1
peakLocations = []
while i < n:
    if (i==0 or height[i] > height[i-1]) and (i==n-1 or height[i] > height[i+1]):
        peakLocations.append(i)
    i += 1

for i in range(len(peakLocations)-1):
    peak1Loc = peakLocations[i]
    peak2Loc = peakLocations[i+1]
    waterLvl = min(height[peak1Loc], height[peak2Loc])
    for j in range(peak1Loc + 1, peak2Loc):
        if height[j] < waterLvl:
            water += waterLvl - height[j]


