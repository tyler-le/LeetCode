class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # dfs in parallel
        # base cases:
        # explore oob in grid 2 but inbounds on grid 1 - not a sub island
        # oob in grid 2
        res = 0
        n, m = len(grid2), len(grid2[0])
        
        # fill island with 0's
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m: 
                return
            
            if grid2[i][j]:
                
                grid2[i][j] = 0
                
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
            

                
            
        
        for i in range(n):
            for j in range(m):
                if not grid1[i][j] and grid2[i][j]: 
                    dfs(i, j)
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j]:
                    dfs(i,j)
                    res+=1
        
        return res