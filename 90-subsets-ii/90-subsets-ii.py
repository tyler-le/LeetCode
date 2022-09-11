class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
     
        
        # BACKTRACKING SOLUTION
        
        
        
        
        def backtrack(i):
            # at each step, we choose to include nums[i] or exclude nums[i]
            
            # base case
            if i >= len(nums):
                res.append(subset*1)
                return
                
            # include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            
            # skip dups
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            # exclude nums[i]
            subset.pop()
            backtrack(i+1)
        
        nums.sort()
        subset, res = [], []
        backtrack(0)
        return res