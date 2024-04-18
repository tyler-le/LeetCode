class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # for each land cell, count how many sides touch water or border
        
        
        def dfs(i, j):
            nonlocal perimeter
            
            # base case
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == WATER: 
                return
            
            if (i,j) in visited:
                return
            
            # handle current cell
            visited.add((i, j))
            
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                if di+i < 0 or dj+j < 0 or i+di >= n or j+dj >= m:
                    perimeter+=1
                elif grid[i+di][j+dj] == WATER:
                    perimeter+=1
                    
            
            # recursive call
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(i+di, j+dj)
        
        n, m = len(grid), len(grid[0])
        perimeter = 0
        LAND, WATER = 1, 0
        visited = set()
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == LAND:
                    dfs(r,c)
                    return perimeter
                