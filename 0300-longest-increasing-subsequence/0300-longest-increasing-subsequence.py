class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        @cache
        def f(i):
            res = 1

            for j in range(i):
                if nums[i] > nums[j]:
                    subproblem = f(j)
                    res = max(res, 1 + subproblem)
            
            return res

        res = 1
        for x in range(len(nums)):
            res = max(res, f(x))
        return res
