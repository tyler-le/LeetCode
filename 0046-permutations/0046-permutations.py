class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for each choice, loop through entirety of nums and backtrack. exclude current number

        res, n, visited = [], len(nums), set()

        def backtrack(path):
            nonlocal res, n 

            if len(path) >= n:
                res.append(path.copy())
                return
            
            for i in range(n):

                if nums[i] in visited: continue
                visited.add(nums[i])
                backtrack(path + [nums[i]])
                visited.remove(nums[i])

        backtrack([])
        return res