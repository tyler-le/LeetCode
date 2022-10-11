class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        
        for i in range(len(nums)):
            mini = maxi = nums[i]
            for j in range(i, len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                res += maxi - mini
                
        return res