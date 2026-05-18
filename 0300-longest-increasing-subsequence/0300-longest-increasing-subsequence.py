class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):

            for j in range(i):
                if nums[i] > nums[j]:
                    subproblem = dp[j]
                    dp[i] = max(dp[i], 1 + subproblem)

        return max(dp)
        

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
