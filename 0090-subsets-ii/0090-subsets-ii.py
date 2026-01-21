class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(index, path):
            nonlocal res, n

            # base case
            if index >= n:
                res.append(path)
                return
            
            # include
            backtrack(index + 1, path + [nums[index]])


            # skip duplicates
            while index + 1 < n and nums[index] == nums[index + 1]:
                index+=1

            # exclude
            backtrack(index + 1, path)
        
        nums.sort()
        backtrack(0, [])
        return res