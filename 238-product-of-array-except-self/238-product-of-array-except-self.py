class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        
        prefix_prod = 1
        output.append(prefix_prod)

        for i in range(1, len(nums)):
            prefix_prod *= nums[i-1]
            output.append(prefix_prod)
            
        postfix_prod = 1
        for i in range(len(nums) - 1, 0, -1):
            postfix_prod *= nums[i]
            output[i-1] = postfix_prod * output[i-1]
        
        return output
            
            
            
            