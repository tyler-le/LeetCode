class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum, max_sum = nums[0], nums[0]
        
        for num in nums[1:]:
            curr_sum+=num
            if curr_sum < num: curr_sum = num
            max_sum = max(max_sum, curr_sum)
                
        return max_sum
            