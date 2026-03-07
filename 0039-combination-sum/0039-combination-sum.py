class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, n = [], len(nums)

        def backtrack(index, curr_path):
            nonlocal res, n

            if index == n: return

            if sum(curr_path) == target: 
                res.append(curr_path.copy())
                return
            
            if sum(curr_path) > target: 
                return

            for i in range(index, n):
                backtrack(i, curr_path + [nums[i]])

        backtrack(0, [])
        return res