class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        # map matrix[index] -> number of ones / zeros
        zeros_row = defaultdict(int)
        zeros_col = defaultdict(int)
        ones_row = defaultdict(int)
        ones_col = defaultdict(int)
        
        n, m = len(grid), len(grid[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]: 
                    ones_row[i]+=1
                    ones_col[j]+=1
                else: 
                    zeros_row[i]+=1
                    zeros_col[j]+=1
            
        for i in range(n):
            for j in range(m):
                res[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        
        return res
        
        