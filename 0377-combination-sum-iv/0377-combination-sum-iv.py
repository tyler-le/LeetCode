class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        DP
        dp[i] = number of ways to make target i
        """
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        
        return dp[target]


        """
        RECURSION + MEMOIZATION
        f(x) = number of ways to make x
        """
        res = 0
        cache = {}
        def f(x):
            cnt = 0

            if x <= 0: 
                if x == 0: return 1
                return 0
            
            if x in cache: return cache[x]

            for num in nums:
                cnt+=f(x - num)

            cache[x] = cnt
            return cnt

        return f(target)
