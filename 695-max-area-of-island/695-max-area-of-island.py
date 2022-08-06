class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i < 0 or j < 0 or i == ROWS or j == COLS or grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            
            return area
            
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(dfs(i,j), res)
                    
        return res