class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = set()


        def f(i, path):
            nonlocal res
            if i == n: 
                res.append(path.copy())
                return

            for j in range(n):
                if j in visited: continue
                visited.add(j)
                f(i+1, path + [nums[j]])
                visited.remove(j)

        f(0, [])
        return res