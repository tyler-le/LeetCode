class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # the min element is the only number smaller than its previous
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
            if mid > low and nums[mid] < nums[mid-1]:
                return nums[mid]
            
            elif mid < high and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[low] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
                
        return nums[0]
                
            