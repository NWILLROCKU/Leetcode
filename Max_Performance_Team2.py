class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eff = []
        mates = []
        maxPerf = 0
        for c1 in range(n):
            myEff = efficiency[c1]
            if myEff not in eff:
                # Figure out the fastest team possible for your efficiency
                eff.append(myEff)
                i = 0
                team = []
                teamSpeeds = []
                for c in range(n):
                    if efficiency[c] > myEff:
                        if i < k: # Just fill team
                            team.append(c)
                            teamSpeeds.append(speed[c])
                            i += 1
                        else: # Can pick and choose
                            if min(teamSpeeds) < speed[c]:
                                swap = teamSpeeds.index(min(teamSpeeds))
                                teamSpeeds[swap] = speed[c]
                                team[swap] = c
                mates.append(team)
            # Get the fastest team possible for your efficiency
            t = eff.index(myEff)
            if c1 in mates[t]:
                team = mates[t]
            else:
                team = [c1] + mates[t][1:]
            perf = 0
            for m in team:
                perf += myEff*speed[m]
            maxPerf = max(maxPerf, perf)          
        
        return int(maxPerf % (1e9 + 7))
