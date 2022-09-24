class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(x, y):
            if x < 0 or y < 0 or x == m or y == n or grid[x][y] =='0' or (x,y) in visited: return
            grid[x][y] = '0'
            visited.add((x,y))
            
            for dx, dy in [(-1, 0), (1,0), (0,-1), (0,1)]:
                r = x+dx
                c = y+dy
                
                dfs(r, c)
                
            
            return
        
        
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res+=1
                    dfs(i,j)
        return res