class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
            
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            biggest = -heapq.heappop(max_heap)
            second_biggest = -heapq.heappop(max_heap)
            
            if biggest != second_biggest:
                heappush(max_heap, -(biggest-second_biggest))
        
        return -heapq.heappop(max_heap) if len(max_heap) == 1 else 0