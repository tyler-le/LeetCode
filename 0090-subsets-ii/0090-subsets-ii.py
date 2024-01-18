class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(idx, path):
            if idx == len(nums):
                res.append(path.copy())
                return
            
            # dfs on future elements with nums[idx] anchored
            backtrack(idx+1, path+[nums[idx]]) 
            
            # skip duplicates from this anchored position 
            # since we already explored all possibilities with nums[idx]
            # that are anchored here
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
                
            # dfs on future elements without nums[idx] anchored
            backtrack(idx+1, path)
        
        res = []
        nums.sort() # to avoid dupes
        backtrack(0, [])
        return res