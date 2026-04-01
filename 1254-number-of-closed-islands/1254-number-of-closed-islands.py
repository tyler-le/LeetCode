class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        LAND, WATER = 0, 1
        visited = set()
        res = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m: return
            if (x, y) in visited: return
            if grid[x][y] == WATER: return

            visited.add((x,y))
            grid[x][y] = WATER

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = x + dx
                c = y + dy
                dfs(r, c)

        # loop on the boundary and turn all LAND to WATER
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
    
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        visited = set()

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == LAND:
                    dfs(i, j)
                    res+=1
        
        return res
            
        