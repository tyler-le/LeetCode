class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1 for _ in range(n)]

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        
        # return max(dp)

        n = len(nums)
        cache = {}

        def f(i):
            if i < 0: return 0
            if i in cache: return cache[i]

            res = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, 1 + f(j))
            
            cache[i] = res
            return res

        res = 1
        for i in range(n):
            res = max(res, f(i))
        return res

        