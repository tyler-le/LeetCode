class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # binary search to find the row
        low, high = 0, len(matrix) - 1
        row_to_search = []

        while low <= high:
            mid = low + ((high - low) // 2)

            mid_row = matrix[mid]

            if mid_row[0] <= target <= mid_row[-1]:
                row_to_search = mid_row
                break

            elif target < mid_row[0]:
                high = mid - 1
            else:
                low = mid + 1

        # search for target within the row
        low, high = 0, len(row_to_search) - 1
        while low <= high:
            mid = low + ((high - low) // 2)

            if row_to_search[mid] < target:
                low = mid + 1
            elif row_to_search[mid] > target:
                high = mid - 1
            else:
                return True
        
        return False
