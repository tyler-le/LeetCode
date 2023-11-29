class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap, res = [], []
        
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        for _ in range(k):
            popped = heapq.heappop(max_heap)
            res.append(-popped)
            
        return res[-1]
            