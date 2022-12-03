class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n;

        dp[0] = nums[0]
        
        for i in range (1,n):
            IN = nums[i] + dp[i-2] if (i > 1) else nums[i]
            OUT = dp[i-1];
            dp[i] = max(IN, OUT);
        
        return dp[n-1];