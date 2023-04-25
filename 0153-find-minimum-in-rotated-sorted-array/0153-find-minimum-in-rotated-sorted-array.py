class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search on the inflection point
        # [4,5,6,7,0,1,2]
        [4,5,6,7,0,1,2]
        
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if nums[mid] > nums[mid+1]: 
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            # left portion is sorted, so search right
            elif nums[low] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
                
        # it is fully sorted already
        return nums[0]
                
            
            