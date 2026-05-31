class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        visited = set()
        nums.sort()

        def f(index, path):
            nonlocal res

            if index == n: 
                res.append(path.copy())
                return

            for j in range(n):
                if j in visited: continue
                if j > 0 and nums[j] == nums[j-1] and j-1 not in visited: 
                    continue
                visited.add(j)
                f(index + 1, path + [nums[j]])
                visited.remove(j)

        f(0, [])
        return res