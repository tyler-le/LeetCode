class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            area = 1
            grid[i][j] = 0
            
            area += dfs(i+1,j)
            area += dfs(i-1,j)
            area += dfs(i,j+1)
            area += dfs(i,j-1)
            return area
            
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
        return res