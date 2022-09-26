class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(combination, nums):
            # if sum too big, stop 
            if sum(combination) > target: 
                return
            
            # if valid combination, add to res
            if sum(combination) == target:
                res.append(combination.copy())
                return
            
            # else for every other number, try to dfs
            for i in range(len(nums)):
                dfs(combination + [nums[i]], nums[i:])
                
        dfs([], candidates)
        return res
                