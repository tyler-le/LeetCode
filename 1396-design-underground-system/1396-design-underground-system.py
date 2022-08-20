
class UndergroundSystem:

    def __init__(self):
        self.ids = {} # map id : (in, time)
        self.routes = defaultdict(int) # map (in, out) : duration
        self.freqs = defaultdict(int) # map (in, out) : count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origin, start = self.ids[id]
        del self.ids[id]
        self.routes[(origin, stationName)] += (t - start)
        self.freqs[(origin, stationName)]+=1
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.routes[(startStation, endStation)] / self.freqs[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)