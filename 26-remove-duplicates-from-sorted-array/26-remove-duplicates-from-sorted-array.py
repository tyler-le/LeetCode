class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,0
        
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[l]:
                r+=1
            
            if r < len(nums):
                l+=1
                nums[l] = nums[r]
                
        return l+1