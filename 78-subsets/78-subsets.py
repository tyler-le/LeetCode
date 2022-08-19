class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, subset):
            if i >= len(nums):
                return res.append(subset.copy())
            
            subset.append(nums[i])
            dfs(i+1, subset)
            
            subset.pop()
            dfs(i+1, subset)
            
            
        visited, res = set(), []
        dfs(0, [])
        return res