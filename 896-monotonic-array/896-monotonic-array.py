class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        increasing, decreasing = False, False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                increasing = True
            if nums[i] > nums[i+1]:
                decreasing = True
        
        if increasing and decreasing:
            return False
        
        return True
        