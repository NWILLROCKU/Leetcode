n = 3
pH = []

def goToNext():
    while pH[-1] != 0:
        pH.pop()
    pH[-1] = 1

# Get final path history
pH_final = []
for i in range(n-1):
    pH_final.append(1)
    pH_final.append(0)

parStrList = []
while 1:
    # Count number of open/closed parentheses
    sumOpen = 1
    sumClosed = 0
    for i in range(len(pH)):
        if pH[i]==0:
            sumOpen += 1
        else:
            sumClosed += 1

    # Reached max # of open par
    if sumOpen==n:
        parStr = '('
        for i in range(len(pH)):
            if pH[i]==0:
                parStr += '('
            else:
                parStr += ')'
        # Fill the rest of the string with ) and add to list
        while len(parStr) < 2*n:
            parStr += ')'
        parStrList.append(parStr)
        
        # If pH==pH_final, end program
        if pH==pH_final:
            break
        
        goToNext()
    elif sumClosed > sumOpen:
        goToNext()
    else:
        pH.append(0)
print(parStrList)
