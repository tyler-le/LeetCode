class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # if it's 0 -> set rows and cols to -1
        
        def set_neg_one(i, j):
            # set row to -1
            for c in range(m):
                matrix[i][c] = "-1" if matrix[i][c] else 0
            
            for r in range(n):
                matrix[r][j] = "-1" if matrix[r][j] else 0
                
        
        n, m = len(matrix), len(matrix[0])
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    set_neg_one(r,c)
                    matrix[r][c] = "-1"
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == "-1":
                    matrix[r][c] = 0
                    
        
        