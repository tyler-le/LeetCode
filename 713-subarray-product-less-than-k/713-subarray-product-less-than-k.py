class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res = 0
        l = 0
        prod = 1
        if k == 0: return 0
        
        for r in range (len(nums)):
            prod *= nums[r]
            while l < r and prod >= k:
                prod /= nums[l]
                l+=1
            if prod < k:
                res += r-l+1
            
        return res