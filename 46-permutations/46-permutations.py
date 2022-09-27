class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = set()
        perms = []
        
        
        def backtrack(perm):
            if len(perm) == len(nums): 
                perms.append(perm[::])
                return
            
            for num in nums:
                if num in visited: continue
                visited.add(num)
                perm.append(num)
                backtrack(perm)
                visited.remove(num)
                perm.pop()
        
        backtrack([])
        return perms