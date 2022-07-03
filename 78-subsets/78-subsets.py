class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        def backtrack(index):
            if index >= len(nums):
                return res.append(subset[:]) # copy
            
            # include nums[index]
            subset.append(nums[index])
            backtrack(index+1)
            
            # exclude nums[index]
            subset.pop()
            backtrack(index+1)
            
        res = [] 
        subset = []
        backtrack(0)
        return res