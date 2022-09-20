class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        max_heap = [-num for num in nums2]
        heapify(max_heap)
        product_sum = 0
        
        for num in nums1:
            product_sum+=(num * -heappop(max_heap))
            
        return product_sum