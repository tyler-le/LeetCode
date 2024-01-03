class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # dfs in parallel
        # base cases:
        # explore oob in grid 2 but inbounds on grid 1 - not a sub island
        # oob in grid 2
        res = 0
        n, m = len(grid2), len(grid2[0])
        
        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= n or j >= m: return True
            
            if grid1[i][j] == 0 and grid2[i][j] == 0: return True
            
            if grid1[i][j] == 1 and grid2[i][j] == 0: return True
            
            if grid1[i][j] == 0 and grid2[i][j] == 1: return False
            
            grid2[i][j] = 0
            
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            
            return left and right and up and down
                
            
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1: 
                    if dfs(i, j): 
                        res+=1
        
        return res