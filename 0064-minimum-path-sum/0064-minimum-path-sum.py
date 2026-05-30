class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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
