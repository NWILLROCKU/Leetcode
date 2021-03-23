class UndergroundSystem(object):

    def __init__(self):
        # Table 1
        self.inID = []
        self.in_t = []
        self.inStation = []
        
        # Table 2
        self.station1 = []
        self.station2 = []
        self.tsum = []
        self.tcnt = []
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.inID.append(id)
        self.inStation.append(stationName)
        self.in_t.append(t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id in self.inID:
            tab1_i = self.inID.index(id)
            i = 0
            while i < len(self.tsum):
                if self.inStation[tab1_i]==self.station1[i] and stationName==self.station2[i]:
                    self.tsum[i] += t - self.in_t[tab1_i]
                    self.tcnt[i] += 1
                    break
                i += 1
            if i==len(self.tsum):
                self.station1.append(self.inStation[tab1_i])
                self.station2.append(stationName)
                self.tsum.append(t - self.in_t[tab1_i])
                self.tcnt.append(1)
            self.inID.pop(tab1_i)
            self.in_t.pop(tab1_i)
            self.inStation.pop(tab1_i)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        i = 0
        while i < len(self.tsum):
            if startStation==self.station1[i] and endStation==self.station2[i]:
                return float(self.tsum[i]) / float(self.tcnt[i])
            i += 1
        return 0
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
