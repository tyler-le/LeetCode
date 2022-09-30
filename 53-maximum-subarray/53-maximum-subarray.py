class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curr_sum = nums[0]
        
        for num in nums[1:]:
            if curr_sum + num < num: 
                curr_sum = num
            else:
                curr_sum+=num
                
            res = max(res, curr_sum)
                
        return res
        