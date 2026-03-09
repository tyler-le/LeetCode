class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        visited = set()
        nums.sort()

        def backtrack(index, path):
            nonlocal res, n

            if index == n: 
                res.append(path.copy())
                return

            for i in range(n):
                if i in visited: continue

                # Make the rule that:
                # You cannot use the second duplicate until the first duplicate has already been used.
                # This helps us avoid duplicates
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                    continue


                visited.add(i)
                path.append(nums[i])
                backtrack(index + 1, path)
                path.pop()
                visited.remove(i)

            
        backtrack(0, [])
        return res
