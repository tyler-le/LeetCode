class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, idx):
            if idx == len(nums):
                res.append(path.copy())
                return
            
            
            cand = nums[idx]
            
            backtrack(path+[cand], idx+1)
            
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
            
            backtrack(path, idx+1)
        
        nums.sort()
        backtrack([], 0)
        return res