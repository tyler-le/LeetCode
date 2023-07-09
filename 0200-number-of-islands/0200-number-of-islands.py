class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n, m, res = len(grid), len(grid[0]), 0
        
        def dfs(r,c):
            
            if r < 0 or c < 0 or r >= n or c >= m:
                return 
            
            if grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return
            
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res+=1
        return res