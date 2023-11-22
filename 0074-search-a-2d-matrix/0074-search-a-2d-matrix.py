class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        low, high = 0, len(matrix) - 1
        
        while low <= high:
            row = low + ((high - low) // 2)
        
            if matrix[row][0] > target: high = row - 1
            elif matrix[row][-1] < target: low = row + 1
            else: break
                
        if row == -1: return False
        
        low, high = 0, len(matrix[row]) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] > target: high = mid - 1
            else: low = mid + 1
                
        return False
            
            