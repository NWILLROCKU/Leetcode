heights = [2,3]
maxA = 0
n = len(heights)
for i in range(len(heights)):
    myH = heights[i]
    barsToRight = 0
    barsToLeft = 0
    if i < n-1: # not at last element
        j = i + 1
        while j < n and heights[j] >= myH:
            barsToRight += 1
            j += 1
    if i > 0: # not first element
        j = i - 1
        while j >= 0 and heights[j] >= myH:
            barsToLeft += 1
            j -= 1
    A = myH * (barsToLeft + 1 + barsToRight)
    maxA = max(maxA, A)
    
