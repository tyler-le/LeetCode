class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r = 0,len(nums) - 1
        res=[]
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.insert(0, nums[l]**2)
                l+=1
            else:
                res.insert(0, nums[r]**2)
                r-=1
        
        return res