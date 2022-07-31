class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
            
        for i in range(k):
            popped = heappop(heap)
            
        return -popped