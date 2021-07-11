class MyCalendar:

    def __init__(self):
        self.times = []

    def book(self, start: int, end: int) -> bool:
        if self.times==[]:
            self.times = [[start, end]]
            return True
        
        # self.times is non-empty
        i = 0
        while start >= self.times[i][1]:
            i += 1
            if i==len(self.times):
                self.times.append([start, end])
                return True
            
        # start < end of self.times[i]
        if end <= self.times[i][0]:
            self.times.insert(i, [start, end])
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
