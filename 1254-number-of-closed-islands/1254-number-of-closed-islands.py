class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def flood_fill(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
                return
            
            grid[i][j] = 1
            
            flood_fill(i+1,j)
            flood_fill(i-1,j)
            flood_fill(i,j+1)
            flood_fill(i,j-1)
            
        # perform flood fill on borders
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if col == 0 or col == len(grid[0]) - 1 or row == 0 or row == len(grid) - 1:
                    flood_fill(row,col)
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
                return
            
            grid[i][j] = 1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        # count remaining islands
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(row,col)
                    res += 1
        return res
        