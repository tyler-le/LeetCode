class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(index, path):
            nonlocal res, n

            if index >= n: 
                res.append(path.copy())
                return 

            IN = backtrack(index + 1, path + [nums[index]])
            OUT = backtrack(index + 1, path)
        
        backtrack(0, [])

        return res
