class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        
        @cache
        def f(i):
            out = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    out = max(out, 1 + f(j))

            return out

        res = 1
        for i in range(len(nums)):
            res = max(res, f(i))

        return res
