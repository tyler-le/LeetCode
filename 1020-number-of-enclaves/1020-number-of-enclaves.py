class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # turn all 1 connected to the boundary to 0
        def handle_boundary(i, j):
            if i < 0 or j < 0 or i >= n or j >= m: return
            if not grid[i][j]: return
            
            grid[i][j] = 0
            
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                handle_boundary(i + di, j + dj)
                
        
        # run number of islands
        def dfs(i, j):
            ans = 0
            if i < 0 or j < 0 or i >= n or j >= m: return ans
            if not grid[i][j]: return ans
            
            grid[i][j] = 0
            ans+=1
            
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ans+=dfs(i + di, j + dj)
            
            return ans
            
            
            
        
        n = len(grid)
        m = len(grid[0])
        res = 0
        
        for r in range(n):
            if grid[r][0]: handle_boundary(r, 0)
            if grid[r][m-1]: handle_boundary(r, m-1)
        
        for c in range(m):
            if grid[0][c]: handle_boundary(0, c)
            if grid[n-1][c]: handle_boundary(n-1, c)
        
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    res+=dfs(r, c)
        
        return res