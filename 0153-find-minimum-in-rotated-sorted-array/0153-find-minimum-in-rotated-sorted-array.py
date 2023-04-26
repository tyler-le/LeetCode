class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # Check if the pivot occurs near mid
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            # Check if the pivot occurs near mid
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            # Left portion is sorted, search for pivot on right
            if nums[low] < nums[mid]:
                low = mid + 1
            # Right portion is sorted, search for pivot on left
            else:
                high = mid - 1
                
        # Pivot never found, array is already sorted
        return nums[0]