class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)

        def backtrack(start, path):

            nonlocal res, n

            # this actually never happens because the for-loop is bounded
            if start > n: return
            
            res.append(path.copy())

            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res