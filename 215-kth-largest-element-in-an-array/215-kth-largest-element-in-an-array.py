class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
      
        max_heap = [-num for num in nums]
        heapify(max_heap)
        
        for _ in range(k):
            kth_largest = heappop(max_heap)
        
        return -kth_largest
        
        