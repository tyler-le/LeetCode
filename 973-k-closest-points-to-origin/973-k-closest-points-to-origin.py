class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for x,y in points:
            # euclidean distance
            dist = math.sqrt(x**2 + y**2)
            # create tuple (dist, x, y)
            to_insert = (dist,x, y)
            heappush(heap, to_insert)
        
        for i in range(k):
            dist,x,y = heappop(heap)
            res.append([x,y])
        return res
        
            