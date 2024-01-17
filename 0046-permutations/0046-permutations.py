class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num not in path:
                    backtrack(path + [num])

            
        backtrack([])
        return res