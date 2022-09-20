class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        # pair biggest in nums2 with smallest from nums1
        # nums2 will have a max-heap and nums1 will have a min-heap
        product_sum = 0
        
        min_heap = nums1
        heapify(nums1)
        
        max_heap = [-num for num in nums2]
        heapify(max_heap)
        
        while min_heap and max_heap:
            x, y = heappop(min_heap), -heappop(max_heap)
            product_sum+=(x*y)
            
        return product_sum