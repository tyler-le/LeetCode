class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]

        # Initialize first column
        for r in range(1, n):
            dp[r][0] = dp[r-1][0] + grid[r][0] 
            
        # Initialize first row
        for c in range(1, m):
            dp[0][c] = dp[0][c-1] + grid[0][c]
            
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = grid[r][c] + min(dp[r][c-1], dp[r-1][c])
                
        return dp[n-1][m-1]
            

        