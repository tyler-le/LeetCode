class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # Check if the pivot occurs near mid
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[low] < nums[mid]:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return nums[0]