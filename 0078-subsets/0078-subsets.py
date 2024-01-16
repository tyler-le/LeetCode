class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return

            backtrack(i+1, path + [nums[i]])
            backtrack(i+1, path)
    
        res = []
        backtrack(0, [])
        return res