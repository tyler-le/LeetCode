class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_set, col_set = set(), set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0