class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = nums[0]
        res = -1
        
        for num in nums[1:]:
            if num - min_so_far > 0:
                res = max(res, num-min_so_far)
            min_so_far = min(min_so_far, num)
        return res