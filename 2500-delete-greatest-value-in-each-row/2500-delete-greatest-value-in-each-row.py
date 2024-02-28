class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        # for each row, delete biggest element
        # of these deleted elements, add the max to res
        res = 0
        
        for row in grid:
            row.sort()
        
        for c in range(len(grid[0])):
            global_max = -1
            
            for r in range(len(grid)):
                global_max = max(global_max, grid[r][c])
            
            res+=global_max
            
            
        
        return res
                