class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        x1 = nums[0]
        for i in range(1, len(nums)):
            x1 ^= nums[i]
        
        return x1
        