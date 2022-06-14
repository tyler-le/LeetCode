class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0
        
        res = l = r = 0
        product = 1
        
        while r < len(nums):
            product *= nums[r]
            
            while product >= k and l <= r:
                product /= nums[l]
                l+=1
                
            res += r - l + 1
            r += 1
        
        return res
        