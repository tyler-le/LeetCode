class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for col in range(m):
            dp[0][col] = 1
        
        for row in range(n):
            dp[row][0] = 1

        dp[0][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                up = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0
                dp[i][j] = up + left
        
        return dp[n-1][m-1]

        