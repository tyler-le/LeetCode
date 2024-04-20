class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def dfs(i, j):
            
            nonlocal res
            
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if land[i][j] == 0:
                return
            
            land[i][j] = 0
            
            res[-1][0] = min(res[-1][0], i)
            res[-1][1] = min(res[-1][1], j)
            res[-1][2] = max(res[-1][2], i)
            res[-1][3] = max(res[-1][3], j)
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        
        n, m = len(land), len(land[0])
        res = []
        
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    res.append([i,j,i,j])
                    dfs(i,j)
        
        return res
            