class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        # dp[i][j] = number of ways to roll i dice with target j
        
        # return dp[n][target]
        
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]        
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                for x in range(1, k+1):
                    if (j-x) >= 0: 
                        dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % (10**9 + 7)
        
        return dp[n][target]
        
    
    
    