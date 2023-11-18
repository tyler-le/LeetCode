class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = -float("inf")
        prod = 1
        
        for i in range(n):
            prod *= nums[i]
            maxi = max(maxi, prod)
            if not prod: prod = 1
         
        prod = 1
        for i in range(n-1, -1, -1):
            prod *= nums[i]
            maxi = max(maxi, prod)
            if not prod: prod = 1
                
        return maxi
                
            
        
        
        