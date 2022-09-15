class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_first_row, zero_first_col = False, False
        
        # determine if we need to zero-out first row
        for i in range(cols): 
            if matrix[0][i] == 0: 
                zero_first_row = True
                break
                
        # determine if we need to zero-out first col
        for i in range(rows):
            if matrix[i][0] == 0: 
                zero_first_col = True
                break
                
        
        # perform flagging on matrix (except first row, first col)
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0: 
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        # start to zero-out besides first row/col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0: 
                    matrix[i][j] = 0
        
        
        # process first col
        if zero_first_col:
            for i in range(rows):
                matrix[i][0] = 0
        
        # process first row
        if zero_first_row:
            for i in range(cols):
                matrix[0][i] = 0
        
        
            
        
            