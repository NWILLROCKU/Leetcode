class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        def getInsInd(num, arr, left, right):
            # Find the index to insert num in the part of 'arr' between indices 'left' and 'right' (inclusive)
            
            middle = int((left+right)/2)
            
            if num==self.arr[middle]:
                return middle
            elif num < self.arr[middle]:
                if middle==left:
                    return left
                return getInsInd(num, arr, left, middle-1) #check
            else: # num > self.arr[middle]
                if middle==right:
                    return right+1
                return getInsInd(num, arr, middle+1, right)
            
        if len(self.arr)==0:
            self.arr.append(num)
        else:
            self.arr.insert(getInsInd(num, self.arr, 0, len(self.arr)-1), num)
        #print(self.arr)
            
        

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2==0:
            return (self.arr[int(n/2)] + self.arr[int(n/2) - 1]) / 2
        else:
            return self.arr[int(n/2)]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
