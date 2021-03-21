def getMinBoats(limit, people):
    import math

    boats = 0
    people.sort()
    j = people[-1]
    while people[-1]==limit:
        people.pop()
        boats += 1
    i = 0
    while len(people) > 0:
        while i < len(people) and people[i] <= limit - people[-1]:
            i += 1
        if i==0:
            people.pop()
            boats += 1
        elif i==len(people): # all people can fit 2 in a boat
            boats += math.ceil(len(people)/2)
            return boats
        else:
            i -= 1
            people.pop()
            people.pop(i)
            boats += 1
    return boats        
