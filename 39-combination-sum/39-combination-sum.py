class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(curr_list, nums):
            if sum(curr_list) > target:
                return
            if sum(curr_list) == target:
                res.append(curr_list.copy())
                return
            
            for i in range(len(nums)):
                dfs(curr_list + [nums[i]], nums[i:])
                
        dfs([], candidates)
        return res
                