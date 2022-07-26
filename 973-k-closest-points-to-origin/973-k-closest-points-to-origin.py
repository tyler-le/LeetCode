class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for x,y in points:
            # euclidean distance
            dist = math.sqrt(x**2 + y**2)
            
            # create tuple (dist, x, y)
            tupl = (dist,x, y)
            heappush(heap, tupl)
        
        for i in range(k):
            _, x, y = heappop(heap)
            res.append([x,y])
            
        return res
        
            