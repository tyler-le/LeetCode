class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # limit max heap to size k
        max_heap = [] # (distance, x, y)

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush_max(max_heap, (dist, x, y))

            if len(max_heap) > k:
                heapq.heappop_max(max_heap)
        
        return [(x, y) for (_, x, y) in max_heap]