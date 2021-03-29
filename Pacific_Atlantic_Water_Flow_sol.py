import collections as coll

num_rows = 5
num_cols = 6
# Setup each queue with cells adjacent to their respective ocean
pacific_queue = coll.deque()
atlantic_queue = coll.deque()
for i in range(num_rows):
    pacific_queue.append((i, 0))
    atlantic_queue.append((i, num_cols - 1))
for i in range(num_cols):
    pacific_queue.append((0, i))
    atlantic_queue.append((num_rows - 1, i))

