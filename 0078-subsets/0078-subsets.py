class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)

        def rec(path, index):
            nonlocal res
            if index == n: 
                res.append(path.copy())
                return 

            # include
            rec(path + [nums[index]], index + 1)


            # exclude
            rec(path, index + 1)



        rec([], 0)
        return res
