class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(combination, nums, curr_sum, index):
            if curr_sum == target:
                res.append(combination[::])
                return
            if curr_sum > target: 
                return
            
            for i in range(len(nums)):
                combination.append(nums[i])
                curr_sum+=nums[i]
                
                backtrack(combination, nums[i:], curr_sum, i)
                
                combination.pop()
                curr_sum-=nums[i]
        
        backtrack([], candidates, 0, 0)
        return res
        
        