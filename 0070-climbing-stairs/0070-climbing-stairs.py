class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
        DP
        """
        dp = [0 for _ in range(n+1)]
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            one_step = dp[i-1]
            two_step = dp[i-2]
            dp[i] = one_step + two_step
        return dp[n]


        """
        RECURSION + MEMOIZATION
        """
        cache = {}
        def f(i):
            if i == 0 or i == 1: return 1
            if i in cache: return cache[i]
            one_step = f(i-1)
            two_step = f(i-2)
            cache[i] = one_step + two_step
            return cache[i]
        return f(n)