class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        row_max, col_max = defaultdict(int), defaultdict(int)
        n = len(grid)
        res = 0

        for i in range(n):
            for j in range(n):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        
        for i in range(n):
            for j in range(n):
                res+=  min(row_max[i], col_max[j]) - grid[i][j]
        
        return res
        
        

        

