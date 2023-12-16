class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                