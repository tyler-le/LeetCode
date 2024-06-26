class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        
        dp = [0 for _ in range(n+1)]
        
        dp[0], dp[1], dp[2] = 0, 1, 1
        
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[-1]