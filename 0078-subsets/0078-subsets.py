class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start, path):
            nonlocal res

            for i in range(start, n):
                path.append(nums[i])
                res.append(path.copy())
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        res.append([])
        return res