class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] = number of unique paths to reach [i][j]
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]

        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        # Initialize the first row and column
        dp[0][0] = 1 - obstacleGrid[0][0]
        for r in range(1, n):
            dp[r][0] = dp[r-1][0] * (1 - obstacleGrid[r][0])
        for c in range(1, m):
            dp[0][c] = dp[0][c-1] * (1 - obstacleGrid[0][c])

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]
