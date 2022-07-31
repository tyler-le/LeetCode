class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        
        # for num in nums:
        #     heappush(heap, -num)
        print(nums)
        for i in range(k):
            popped = heappop(nums)
            
        return -popped