class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        low, high = 0, len(self.hits)-1 
        
        # get low boundary
        while low < len(self.hits) and self.hits[low] <= (timestamp - 300):
            low+=1
        
        # get high boundary
        while high >= 0 and self.hits[high] > (timestamp):
            high-=1

        # since in chronological order, we can get rid of hits[0:low-1] to free space
        # self.hits = self.hits[low:]
        
        # return number of elements within this window
        return high - low + 1
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)