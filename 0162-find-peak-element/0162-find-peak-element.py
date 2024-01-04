class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # [0, 1, 2, 3, 2, 1, 0]
        #           h  
        #           l
        #           m
        
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + ((high - low) // 2)
            
            if nums[mid] < nums[mid+1]: low = mid + 1
            else: high = mid
        
        return high