class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        # for each 1 on the border, run dfs and change to 0
        # then count the number of remaining 1's
        
        n, m, res = len(grid), len(grid[0]), 0
        
        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= n or j >= m: return
            if not grid[i][j]: return
            
            grid[i][j] = 0
            
            left = dfs(i,j-1)
            right = dfs(i,j+1)
            up = dfs(i-1,j)
            down = dfs(i+1,j)
            
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] and i == 0 or i == n-1 or j == 0 or j == m-1:
                    dfs(i, j)
                      
        for i in range(n):
            for j in range(m):
                res+=grid[i][j]

        return res
            