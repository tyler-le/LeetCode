class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # binary search to find appropriate row
        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            mid = top + ((bottom - top) // 2)
            row = matrix[mid]
            
            if target < row[0]: bottom = mid - 1
            elif target > row[-1]: top = mid + 1
            else: break

        # now we have appropriate row so we can look for target        
        low, high = 0, len(row) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            
            if row[mid] == target: return True
            if row[mid] < target: low = mid + 1
            if row[mid] > target: high = mid - 1
                
        return False
            
        