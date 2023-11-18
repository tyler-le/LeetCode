class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        
        for c in range(1, target + 1):
            if c <= k: dp[1][c] = 1
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                for d in range(1, k+1):
                    if j - d >= 0: 
                        dp[i][j] += dp[i-1][j - d]
                        
        return (dp[n][target]) % (10**9 + 7)