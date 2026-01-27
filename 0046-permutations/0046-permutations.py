class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = set()

        def backtrack(path):
            nonlocal res, visited

            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in visited: continue
                visited.add(num)
                backtrack(path + [num])
                visited.remove(num)


        backtrack([])
        return res