class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(idx, path):
            if idx == len(nums):
                res.append(path.copy())
                return
            
            backtrack(idx+1, path+[nums[idx]])
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
            backtrack(idx+1, path)
        
        res = []
        nums.sort()
        backtrack(0, [])
        return res