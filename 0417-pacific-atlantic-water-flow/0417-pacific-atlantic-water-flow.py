class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        
        # start from the edges of pacific and atlantic
        # dfs, visiting nodes that are strictly greater and add to set
        
        def dfs(i, j, ocean_set):
            if (i, j) in ocean_set: return
            
            ocean_set.add((i,j))
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if i+dx < 0 or j+dy < 0 or i+dx >= n or j+dy >= m: continue
                if heights[i][j] <= heights[i+dx][j+dy]:
                    dfs(i+dx, j+dy, ocean_set)
            
        
        
        n, m = len(heights), len(heights[0])
        
        for i in range(n):
            for j in range(m):            
                if j == 0 or i == 0: dfs(i, j, pacific)
                if i == n-1 or j == m-1: dfs(i, j, atlantic)
                
        return pacific.intersection(atlantic)