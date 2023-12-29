class UndergroundSystem:

    def __init__(self):
        self.check_in={}
        self.average={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]=[stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station=self.check_in[id][0]+'-'+stationName
        time=t-self.check_in[id][1]

        if station not in self.average:
            self.average[station]=[time,1]
        else:
            self.average[station][0]+=time
            self.average[station][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time,nums=self.average[startStation+'-'+endStation]
        return time/nums


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)