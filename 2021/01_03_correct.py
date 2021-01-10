from itertools import permutations

n = 9
Arr = list(permutations( list(range(1, n+1)) ))
print('Got perms!')
m = len(Arr)
j = 0
arrCnt = 0
while j < m:
    arr = Arr[j]
    for i in range(len(arr)):
        if (arr[i] % (i+1)) != 0 and ((i+1) % arr[i]) != 0:
            Arr.remove(arr)
            break
        if i==len(arr)-1:
            arrCnt += 1

    j += 1
print(arrCnt)
    
        
