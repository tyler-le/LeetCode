class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap: return [i, hmap[complement]]
            else: hmap[nums[i]] = i