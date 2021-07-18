class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def countZeros(i0):
            # Starting with index i0, find the soonest non-zero index i
            i = i0
            while arr[i]==0:
                i += 1
            return i
        
        def countOnes(i0, oneCnt):
            # Find soonest index i after i0 s.t. (number of ones encountered BEFORE i) == oneCnt
            i = i0
            myOneCnt = 0
            while myOneCnt < oneCnt:
                if arr[i]==1:
                    myOneCnt += 1
                i += 1
            return i
        
        oneCnt = sum(arr)
        false = [-1, -1]
        if oneCnt % 3 != 0:
            return false
        oneCnt = oneCnt / 3
        
        try:
            i0 = countZeros(0)
        except:
            return [0,2]
        i = countOnes(i0, oneCnt)
        j0 = countZeros(i)
        j = countOnes(j0, oneCnt)
        if arr[i0:i] != arr[j0:j]:
            return false
        k0 = countZeros(j)
        k = countOnes(k0, oneCnt)
        if arr[k0:k] != arr[j0:j]:
            return false
        return [i-1, j]
            
        
