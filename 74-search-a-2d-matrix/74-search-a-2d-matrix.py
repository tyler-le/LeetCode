class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # create an array of the elems in sorted order
        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                nums.append(matrix[i][j])
        
        # run binary search on resulting array
        print(nums)
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target: return True
            if nums[mid] < target: low = mid + 1
            if nums[mid] > target: high = mid - 1
        return False
    
        
        