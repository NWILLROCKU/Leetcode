from itertools import permutations

Arr = []
n = 4
for i in range(n):
    original = list(range(1, n+1))
    original[i] = 1
    original[0] = i+1
    Arr.append(list(permutations(original[1:])))
j = 0
arrCnt = 0
while j < len(Arr):
    arr = Arr[j]
    for i in range(len(arr)):
        if (arr[i] % (i+1)) != 0 and ((i+1) % arr[i]) != 0:
            Arr.remove(arr)
            break
        if i==len(arr)-1:
            arrCnt += 1
    j += 1
print(arrCnt)
    
        
