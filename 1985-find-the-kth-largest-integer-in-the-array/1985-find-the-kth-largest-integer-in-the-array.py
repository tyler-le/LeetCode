class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        max_heap = [-int(num) for num in nums]
        heapify(max_heap)
        
        for _ in range(k-1):
            heappop(max_heap)
        
        return str(-max_heap[0])
            
        
        