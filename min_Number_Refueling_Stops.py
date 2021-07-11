class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        i_cur = -1
        odo = 0
        tank = startFuel
        
        n = len(stations)
        
        i = 0
        numStops = 0
        while i < n:
            if stations[i][0] - odo > tank: # can only get to station i-1
                # Find station with highest net benefit
                bestStat = -1
                bestScore = 0
                for i in range(i-1, i_cur, -1):
                    score = stations[i][0] - odo + stations[i][1]
                    if score > bestScore:
                        bestScore = score
                        bestStat = i
                if bestScore==0:
                    return -1
                i_cur = bestStat
                numStops += 1
                odo = stations[i_cur][0]
                tank += stations[i_cur][1]
                i = i_cur
            i += 1
        return numStops
