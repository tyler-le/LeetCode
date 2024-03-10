class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or j < 0: return 0
            if i >= n or j >= m: return 0
            if not grid[i][j]: return 0
            
            cnt = 1
            grid[i][j] = 0
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r, c = i+dx, j+dy
                cnt+=dfs(r,c)
            
            return cnt
                
        
        n, m = len(grid), len(grid[0])
        res = -math.inf
        for i in range(n):
            for j in range(m):
                if grid[i][j]: 
                    res = max(res, dfs(i, j))
        
        return res if res != -math.inf else 0