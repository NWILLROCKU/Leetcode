limit = 5
people= [1,2,2,3,4,5]

def removeOne(weights, cnt, i):
    cnt[i] -= 1
    if cnt[i]==0:
        cnt.pop(i)
        weights.pop(i)

def getMinBoats(limit, people):
    import math
    boats = 0

    # First take out people who are at the weight limit, one at a time
    while limit in people:
        people.remove(limit)
        boats += 1

    # Build table of unique weights (1 column) and count (2nd column)
    weights = list(set(people))
    cnt = []
    for weight in weights:
        cnt.append(people.count(weight))

    while len(weights) > 0: # weights has 2 or more elements
        w1 = weights[-1]
        w2max = limit - w1
        j = 0
        while j < len(weights) and weights[j] <= w2max:
            j += 1

        if j==0: # no weight is <= w2max
            boats += cnt[-1]
            cnt.pop()
            weights.pop()
        elif j==len(weights): # greatest element of weights <= w2max...meaning all elements in weights can be paired
            boats += math.ceil(sum(cnt)/2)
            return boats
        else: # j is the index of the first element in weights to be > w2max
            j -= 1
            removeOne(weights, cnt, -1)
            removeOne(weights, cnt, j)
            boats += 1
    return boats
                
        
    
    
