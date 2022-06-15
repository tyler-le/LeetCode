class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r, index = 0, len(nums)-1, 0
        
        while index <= r:
            if nums[index] == 0:
                temp = nums[l]
                nums[l] = nums[index]
                nums[index] = temp
                l+=1
                
            elif nums[index] == 2:
                temp = nums[r]
                nums[r] = nums[index]
                nums[index] = temp
                r-=1
                index-=1
                    
            index+=1