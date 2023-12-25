class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
     
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        res = 0
        
        # loop thru rows
        for row in grid:
            rows[tuple(row)]+=1
        
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
                
            if tuple(col) in rows:
                res+= (rows[tuple(col)])
            
                
        return res
        
        
     
        
                
   