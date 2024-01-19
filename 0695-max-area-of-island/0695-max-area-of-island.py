class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            
            
            
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            
            if not grid[i][j]: 
                return 0
            
            cnt = 1
            grid[i][j] = 0
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                cnt+=dfs(dx + i, dy + j)
            
            return cnt
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
                    
        return res