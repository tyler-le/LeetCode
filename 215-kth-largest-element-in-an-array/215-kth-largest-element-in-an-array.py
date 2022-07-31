class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)

        for i in range(k): popped = heappop(nums)
            
        return -popped