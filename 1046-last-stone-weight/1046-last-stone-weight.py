class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-s for s in stones]
        heapify(max_heap)
        
        while len(max_heap) > 1:
            y, x = -heappop(max_heap), -heappop(max_heap)
            
            if x!=y: heappush(max_heap, -(y-x))
        
        return -max_heap[0] if len(max_heap) else 0
            