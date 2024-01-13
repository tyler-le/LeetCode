class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        
        for i in range(n):
            for x in range(1, nums[i]+1):
                if i + x < n:
                    dp[i+x] = min(dp[i+x], 1 + dp[i])
        
        print(dp)
        return dp[n-1]