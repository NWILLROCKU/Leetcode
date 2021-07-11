class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Sort speed & efficiency by efficiency (descending order)
        speed = [x for (y,x) in sorted(zip(efficiency,speed), key=lambda pair: pair[0])] # Sort speeds by efficiency (Note: should work for multiple arrays as well)
        efficiency.sort()
        efficiency.reverse()
        speed.reverse()
        
        maxPerf = 0
        for i in range(k):
            perf = efficiency[i]*sum(speed[:i+1])
            maxPerf = max(maxPerf, perf)
        maxSpeeds = speed[:k]
        for i2 in range(i+1, n):
            if speed[i2] > min(maxSpeeds):
                maxSpeeds.remove(min(maxSpeeds))
                maxSpeeds.append(speed[i2])
                perf = efficiency[i2]*sum(maxSpeeds)
                maxPerf = max(maxPerf, perf)
        return int(maxPerf % (1e9 + 7))
