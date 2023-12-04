class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        res = 0
        
        for _ in range(k):
            popped = -heapq.heappop(max_heap)
            res += popped
            heapq.heappush(max_heap, -ceil(popped / 3))
        
        return res