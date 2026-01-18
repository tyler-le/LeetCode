class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        def backtrack(path, index):
            nonlocal res, n

            if index >= n:
                res.append(path.copy())
                return
            
            # include nums[index]
            backtrack(path + [nums[index]], index + 1)

            # once we've included nums[index] in our subset, 
            # we've explored all choices with nums[index] anchored 
            # at this position in our path
            while (index + 1 < n) and (nums[index] == nums[index + 1]):
                index+=1
            

            # so when we exlude nums[index], 
            # we should not explore any more choices with nums[index]
            # hence we need to skip them
            backtrack(path, index + 1)

        nums.sort()
        backtrack([], 0)
        return res