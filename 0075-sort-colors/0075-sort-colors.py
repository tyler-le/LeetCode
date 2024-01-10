class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if not nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        
        l = len(nums) - 1
        for r in range(len(nums)-1, -1, -1):
            if nums[r] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                l-=1
                