class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] = min falling path at matrix[i][j]
        # dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        # return min(dp[n-1][col]) for all col
        
        n = len(matrix)
        
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]  
        
        for col in range(n):
            dp[0][col] = matrix[0][col]
        
        for i in range(1,n):
            for j in range(n):
                first = dp[i-1][j-1] if j-1 >= 0 else float("inf")
                second = dp[i-1][j] 
                third = dp[i-1][j+1] if j+1 < n else float("inf")
                dp[i][j] = matrix[i][j] + min(first, second, third)
        print(dp)       
        return min(dp[n-1])