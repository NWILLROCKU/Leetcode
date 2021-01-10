import math

def inList(smaller, larger):
    # Check if the smaller list of numbers is in the larger
    for i in smaller:
        if i not in larger:
            return False
    return True

beautGrps = [[1], [1,2], [1,3], [1,2,4], [1,5], [1,2,6], [1,3,6],
             [1,7], [1,2,4,8], [1,3,9], [1,2,10], [1,5,10], [1,11],
             [1,2,6,12], [1,3,6,12], [1,2,4,12], [1,13], [1,2,14],
             [1,7,14], [1,3,15], [1,5,15]]

numNewArr = [] # number of new arrangements contributed by each member of beautGrps
for i in range(len(beautGrps)):
    currGroup = beautGrps[i]
    numNewArr.append( math.factorial(len(currGroup)) )
    for j in range(i):
        if inList(beautGrps[j], currGroup):
            numNewArr[-1] -= numNewArr[j]

def countBeautifulArr(n):            
    baCnt = 0
    for i in range(len(beautGrps)):
        if beautGrps[i][-1] > n:
            return baCnt
        baCnt += numNewArr[i]        
        
