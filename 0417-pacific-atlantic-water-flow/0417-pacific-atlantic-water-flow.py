class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        n, m = len(heights), len(heights[0])
        
        def dfs(r, c, s, prev):
            if r < 0 or c < 0 or r >= n or c >= m:
                return
            
            if (r,c) in s:
                return
            
            if prev > heights[r][c]:
                return
            
            s.add((r,c))
            
            dfs(r+1,c,s, heights[r][c])
            dfs(r-1,c,s, heights[r][c])
            dfs(r,c+1,s, heights[r][c])
            dfs(r,c-1,s, heights[r][c])
            
        
        # gather all nodes reachable from pacific
        for row in range(n):
            dfs(row, 0, pac, heights[row][0])
        for col in range(m):
            dfs(0, col, pac, heights[0][col])
            
        # gather all nodes reachable from atlantic
        for row in range(n):
            dfs(row, m-1, atl, heights[row][m-1])
        for col in range(m):
            dfs(n-1, col, atl, heights[n-1][col])
            
        return pac.intersection(atl)
    
        
        