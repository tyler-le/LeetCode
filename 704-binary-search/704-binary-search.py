class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(nums, target, low, high):
            
            if high < low: return -1        
            mid = low + (high - low) / 2
    
            if nums[mid] < target: return helper(nums, target, mid+1, high)
            elif nums[mid] > target: return helper(nums,target, low, mid-1)
            else: return mid
            
        
        return helper(nums, target, 0, len(nums)-1)