class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
       # 2 pass solution
        # first move all zeroes to left
        # second more twos to right
        
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
                zero_pos+=1
        
        two_pos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 2:
                nums[two_pos], nums[i] = nums[i], nums[two_pos]
                two_pos-=1
        