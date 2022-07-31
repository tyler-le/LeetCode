class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        num_rows, num_cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        
        def dfs(r, c, visit, prev_height):
            if ((r,c) in visit
               or r < 0
               or c < 0
               or r == num_rows
               or c == num_cols
               or heights[r][c] < prev_height):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        
        for r in range(num_rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, num_cols-1, atlantic, heights[r][num_cols-1])
            
        for c in range(num_cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(num_rows-1, c, atlantic, heights[num_rows-1][c])
            
        return list(pacific.intersection(atlantic))