class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heappush(heap, -num)
            
        for i in range(k):
            popped = heappop(heap)
            
        return -popped
        