class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        num_zero, num_one, num_two = 0,0,0
        
        for num in nums:
            if num == 0:
                num_zero+=1
                
            elif num == 1:
                num_one+=1
                
            else:
                num_two+=2
                
        
        for index in range(len(nums)):
            if num_zero > 0:
                nums[index] = 0
                num_zero-=1
                
            elif num_one > 0:
                nums[index] = 1
                num_one-=1
                
            else:
                nums[index] = 2
                num_two-=1
                
    
        