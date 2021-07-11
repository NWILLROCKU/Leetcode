# Attempt 2
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        per = sum(matchsticks)
        if per % 4 != 0:
            return False
        sideLen = per / 4
        if sideLen < max(matchsticks):
            return False
        matchsticks.sort()
        
        sidesum = [0]*4
        skipped = side = 0
        while len(matchsticks) > 0:
            if skipped==len(sidesum):
                return False
            
            if sidesum[side] + matchsticks[-1] <= sideLen:
                sidesum[side] += matchsticks.pop()
                if sidesum[side]==sideLen:
                    sidesum.pop(side)
                else:
                    side += 1
                if side==len(sidesum):
                    side = 0
                skipped = 0
            else:
                skipped += 1
        return True
                

# Attempt 1
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        per = sum(matchsticks)
        if per % 4 != 0:
            return False
        sideLen = per / 4
        if sideLen < max(matchsticks):
            return False
        matchsticks.sort(reverse=True)
        
        i = sideTot = numSides = 0
        while len(matchsticks) > 0:
            if sideTot + matchsticks[i] <= sideLen:
                sideTot += matchsticks[i]
                print(matchsticks.pop(i))
                if sideTot==sideLen:
                    numSides += 1
                    sideTot = i = 0
            else:
                if i < len(matchsticks)-1:
                    i += 1
                else:
                    return False
        if numSides==4 and sideTot==0:
            return True
        return False
            
