class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        DP
        """
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            one_step = dp[i-1]
            two_step = dp[i-2] + nums[i]
            dp[i] = max(one_step, two_step)

        return dp[n-1]
        
        
        """
        RECURSION + MEMOIZATION
        """
        n = len(nums)
        cache = {}
        def f(i):
            if i < 0: return 0
            if i == 0: nums[0]
            if i == 1: max(nums[0], nums[1])
            if i in cache: return cache[i]
            one_step = f(i-1)
            two_step = f(i-2) + nums[i]
            cache[i] = max(one_step, two_step)
            return cache[i]
        return f(n-1)