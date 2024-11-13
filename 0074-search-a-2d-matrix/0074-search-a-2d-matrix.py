class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(curr_row, left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if target > curr_row[mid]: 
                    left = mid + 1
                elif target < curr_row[mid]:
                    right = mid - 1
                else:
                    return True
            return False
                    
            
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        
        # find the appropriate row
        while top <= bottom:
            mid = top + (bottom - top) // 2
            curr_row = matrix[mid]
            
            if target < curr_row[0]:
                bottom = mid - 1
                
            elif curr_row[0] <= target <= curr_row[-1]:
                return binary_search(curr_row, 0, len(curr_row) - 1, target)

            else:
                top = mid + 1
        
        return False