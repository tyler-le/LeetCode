class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] = number of ways to reach sum i
        # return dp[target]
        
        dp = [0] * (target+1)
        dp[0] = 1
        
        for i in range(1, len(dp)):
            for num in nums:
                dp[i] += dp[i-num] if i - num >= 0 else 0
        
        return dp[target]