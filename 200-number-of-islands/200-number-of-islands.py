class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
        
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res+=1
                    dfs(i,j)
        return res