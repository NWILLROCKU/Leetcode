def minCost(i):
    if i==0 or i==1:
        return cost[i]
    else:
        return cost[i] + min(minCost(i-1), minCost(i-2))
