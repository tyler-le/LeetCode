class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = set()
        res = []
        n = len(nums)

        def backtrack(path):
            # base case
            if len(path) == n:
                res.append(path.copy())
                return
            
            for num in nums:
                if num in visited: continue

                visited.add(num)
                path.append(num)

                backtrack(path)

                path.pop()
                visited.remove(num)
        
        backtrack([])
        return res