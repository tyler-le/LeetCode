class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        min_heap = []
        res = []
        
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            min_heap.append((dist, x, y))
            
        heapify(min_heap)
        
        for i in range(k):
            popped = heappop(min_heap)
            res.append([popped[1], popped[2]])
        
        return res