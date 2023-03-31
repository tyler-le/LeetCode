class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1): return nums[0]
        if (n == 2): return max(nums[0], nums[1])
        
        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n+1):
            IN = dp[i-2] + nums[i] if i < n else dp[i-2]
            OUT = dp[i-1]
            dp[i] = max(IN, OUT)
            
        return dp[-1]