import heapq

# Inputs
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

modulo = 10 ** 9 + 7

# build tuples of (efficiency, speed)
candidates = zip(efficiency, speed)
# sort the candidates by their efficiencies
candidates = sorted(candidates, key=lambda t:t[0], reverse=True)

speed_heap = []
speed_sum, perf = 0, 0
for curr_efficiency, curr_speed in candidates:
    # maintain a heap for the fastest (k-1) speeds
    if len(speed_heap) > k-1:
        speed_sum -= heapq.heappop(speed_heap)
    heapq.heappush(speed_heap, curr_speed)
    print(speed_heap)

    # calculate the maximum performance with the current member as the least efficient one in the team
    speed_sum += curr_speed
    perf = max(perf, speed_sum * curr_efficiency)

print( perf % modulo)
