class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for x,y in points:
            dist = math.sqrt(x**2 + y**2) # euclidean distance
            heap.append([dist,x, y])
            
        heapify(heap) # heapify at end is faster than heappush
        
        for i in range(k):
            _, x, y = heappop(heap)
            res.append([x,y])
            
        return res
        
            