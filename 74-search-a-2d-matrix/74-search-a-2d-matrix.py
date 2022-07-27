class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # binary search to find row
        num_rows, num_cols = len(matrix) - 1, len(matrix[0]) - 1
        
        low, high = 0, num_rows
        while low <= high:
            mid = low + ((high - low) // 2)
            row_to_search = matrix[mid]
            if target < row_to_search[0]: high = mid - 1
            elif target > row_to_search[-1]: low = mid + 1
            else: break

        low, high = 0, len(row_to_search) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if row_to_search[mid] == target: return True
            if row_to_search[mid] < target: low = mid + 1
            if row_to_search[mid] > target: high = mid - 1
        return False
            
        