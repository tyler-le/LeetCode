class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = [-num for num in nums]
        heapify(max_heap)
        
        for _ in range(k-1):
            heappop(max_heap)
        
        return -heappop(max_heap)