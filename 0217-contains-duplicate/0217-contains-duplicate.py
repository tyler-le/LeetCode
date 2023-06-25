class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        
        for num in nums:
            if num in visited: return True
            visited.add(num)
            
        return False