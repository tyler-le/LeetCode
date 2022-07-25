class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            if curr_sum + nums[i] < nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
                
            res = max(curr_sum, res)
                
        res = max(curr_sum, res)
        return res