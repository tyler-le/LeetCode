class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums: continue
            count = 0
            while num in nums:
                count+=1
                num+=1
                
            res = max(res, count)
                
                
                
        return res