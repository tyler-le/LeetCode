class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n, OBSTACLE = len(obstacleGrid), len(obstacleGrid[0]), 1
        
        # edge case - if start/goal is an obstacle
        if obstacleGrid[0][0] == OBSTACLE: return 0
        if obstacleGrid[m-1][n-1] == OBSTACLE: return 0

        dp = [[0 for c in range(n)] for r in range(m)]
        # Set the first cell
        dp[0][0] = 0 if obstacleGrid[0][0] == OBSTACLE else 1

        # Initialize the first column
        for r in range(1, m): 
            dp[r][0] = 0 if obstacleGrid[r][0] == OBSTACLE or dp[r-1][0] == 0 else 1

        # Initialize the first row
        for c in range(1, n): 
            dp[0][c] = 0 if obstacleGrid[0][c] == OBSTACLE or dp[0][c-1] == 0 else 1

#         for r in range(m): 
#             if obstacleGrid[r][0] == OBSTACLE: 
#                 dp[r][0] = 0
#             else:
#                 dp[r][0] = 1
                
#         for c in range(n): 
#             if obstacleGrid[0][c] == OBSTACLE:
#                 dp[0][c] = 0
#             else:
#                 dp[0][c] = 1

        print(dp)
        
        for i in range(1,m):
            for j in range(1,n):
                left = 0 if obstacleGrid[i-1][j] == OBSTACLE else dp[i-1][j]
                up = 0 if obstacleGrid[i][j-1] == OBSTACLE else dp[i][j-1]
                dp[i][j] = left + up
                
        # print(dp)       
        return dp[m-1][n-1]