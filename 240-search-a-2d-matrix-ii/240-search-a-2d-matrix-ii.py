class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row):
            low, high = 0, len(row)-1
            while low <= high:
                mid = low + ((high - low) // 2)
                
                if target < row[mid]: high = mid - 1
                elif target > row[mid]: low = mid + 1
                else: return True
                
            return False
            
        for row in matrix:
            if binary_search(row): return True
        return False