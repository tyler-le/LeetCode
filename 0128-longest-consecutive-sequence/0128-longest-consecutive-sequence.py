class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bag = set(nums)
        ret = 0

        for num in nums:
            if num-1 in bag: continue
            count = 0
            curr = num
            while curr in bag:
                curr+=1
                count+=1
            ret = max(ret, count)      
        return ret
                
        