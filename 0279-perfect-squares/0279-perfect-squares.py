class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = least number of perfect square that sum to i
        
        dp = [float("inf") for _ in range(n+1)]
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(len(dp)):
            square = 1
            
            while square * square <= i:
                dp[i] = min(dp[i], 1 + dp[i-(square*square)])
                square+=1
        
        return dp[n]