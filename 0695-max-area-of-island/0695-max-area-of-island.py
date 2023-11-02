class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols, res = len(grid), len(grid[0]), 0
        
        def dfs(row, col):
            area = 1
            
            if row < 0 or row >= rows \
                or col < 0 or col >= cols \
                or not grid[row][col]:
                return 0
            
            grid[row][col] = 0
            area+=dfs(row+1, col)
            area+=dfs(row-1, col)
            area+=dfs(row, col+1)
            area+=dfs(row, col-1)
            
            return area
            
            
        
        for r in range(rows):
            for j in range(cols):
                if grid[r][j] == 1:
                    res = max(res, dfs(r, j))
        
        return res
        