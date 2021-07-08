class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x in arr:
            i = j = arr.index(x)
        elif x < arr[0]:
            return arr[:k]
        elif arr[-1] < x:
            return arr[-k:]
        else:
            j = 1
            while x > arr[j]:
                j += 1
            i = j-1
            # Now, arr[i] < x < arr[j]
            if x - arr[i] <= arr[j] - x:
                j = i
            else:
                i = j
        
        while j - i + 1 < k:
            if i==0:
                return arr[:k]
            if j==len(arr)-1:
                return arr[-k:]
            if x - arr[i-1] <= arr[j+1] - x:
                i -= 1
            else:
                j += 1
        
        return arr[i:j+1]
