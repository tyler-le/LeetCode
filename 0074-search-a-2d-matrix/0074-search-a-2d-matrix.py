class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_to_search = []
        
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if matrix[mid][0] > target: high = mid - 1
            elif matrix[mid][-1] < target: low = mid + 1
            else: 
                row_to_search = matrix[mid]
                break
                
                
        low, high = 0, len(row_to_search) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if row_to_search[mid] == target: return True
            elif row_to_search[mid] > target: high = mid - 1
            else: low = mid + 1
                
        return False
            
            