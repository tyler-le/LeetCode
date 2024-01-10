class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        seen = set()
        
        for start, end in nums:
            for i in range(start, end+1):
                seen.add(i)
        return len(seen)
        