class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum, max_sum = 0, -float('inf')
        
        for num in nums:
            if num > curr_sum + num: 
                curr_sum = num
                
            else:
                curr_sum += num
            
            max_sum = max(curr_sum, max_sum)
            
        return max_sum
        