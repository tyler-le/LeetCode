class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        if len(nums)==1:
            return 0
        while low < high:
            mid = (high + low) // 2
            
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid
        
        return low