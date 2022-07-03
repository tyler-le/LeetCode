class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # BACKTRACKING SOLUTION
        
        def backtrack(i):
            if i >= len(nums):
                return res.append(subset*1) # make a copy
            
            # include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
                
            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            # exclude nums[i]
            subset.pop()
            backtrack(i+1)

        nums.sort()
        subset, res = [], []
        backtrack(0)
        return res
        