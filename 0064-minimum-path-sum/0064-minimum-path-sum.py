class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        """
        DP
        """
        n, m = len(grid), len(grid[0])
        dp = [[math.inf for _ in range(m)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                cost = grid[i][j]
                if i == n-1 and j == m-1: 
                    dp[i][j] = cost
                    continue
                right_cost = dp[i][j+1] if j+1 < m else math.inf
                down_cost = dp[i+1][j] if i+1 < n else math.inf
                dp[i][j] = cost + min(right_cost, down_cost)

        return dp[0][0]
        
        """
        Recursive
        """
        n, m = len(grid), len(grid[0])

        @cache
        def backtrack(i, j):
            
            if i < 0 or j < 0 or i >= n or j >= m: 
                return math.inf

            cost = grid[i][j]
            
            if i == n-1 and j == m-1: 
                return cost
            
            right_cost = backtrack(i, j+1)
            down_cost = backtrack(i+1, j)

            return cost + min(right_cost, down_cost)

        return backtrack(0, 0)
