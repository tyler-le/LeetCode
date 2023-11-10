class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # Initialize the first row
        dp[0] = matrix[0]
        
        for r in range(1, n):
            for c in range(n):
                
                # up and up-right
                if c == 0:
                    up, up_right = dp[r-1][c], dp[r-1][c+1]
                    dp[r][c] = matrix[r][c] + min(up, up_right)
                
                # up and up-left
                elif c == (n-1):
                    up, up_left = dp[r-1][c], dp[r-1][c-1]
                    dp[r][c] = matrix[r][c] + min(up, up_left)
                
                # up-left and up and up-right
                else:
                    up_left, up, up_right = dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]
                    dp[r][c] = matrix[r][c] + min(up_left, up, up_right)
                    
        return min(dp[-1])