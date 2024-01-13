class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        
        for i in range(n-2, -1, -1):
            for x in range(1, nums[i]+1):
                if x + i < n:
                    dp[i] = dp[x+i] or dp[i]
                    if dp[i]: break
        
        return dp[0]