class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        memo = [-1 for _ in range(len(nums))]
        memo[0], memo[1] = nums[0], max(nums[0], nums[1])
    
        for i in range(2, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])
            
        return memo[-1]
            
