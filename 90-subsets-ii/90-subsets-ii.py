class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # BACKTRACKING SOLUTION
        
        def backtrack(i, subset):
            if i >= len(nums):
                return res.append(subset[::]) # copy
            
            # include nums[i] if not duplicate
            subset.append(nums[i])
            backtrack(i+1, subset)
                
            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            # exclude nums[i]
            subset.pop()
            backtrack(i+1, subset)

        nums.sort()
        subset, res = [], []
        backtrack(0, subset)
        return res
        