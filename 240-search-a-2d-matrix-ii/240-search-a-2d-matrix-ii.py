class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 'Search space reduction' by starting at bottom left
        
        # matrix[i][j] < target then row--
        # matrix[i][j] > target then col++
        
        rows, cols = len(matrix), len(matrix[0])
        
        # start at bottom left
        curr_x, curr_y = rows-1, 0
        
        while (curr_x >= 0) and (curr_y < cols):
            if matrix[curr_x][curr_y] > target: curr_x-=1
            elif matrix[curr_x][curr_y] < target: curr_y+=1
            else: return True
    
        return False