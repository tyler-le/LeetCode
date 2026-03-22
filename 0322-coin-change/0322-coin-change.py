class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        DP
        """
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != math.inf:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[amount] if dp[amount] != math.inf else -1


        """
        RECURSIVE + MEMOIZATION
        """
        cache = {}
        # return min number of ways to get to this target

        def f(target):
            res = math.inf

            if target == 0: return 0

            if target in cache: 
                return cache[target]
            
            for coin in coins:
                if target - coin >= 0:
                    subproblem = f(target - coin)
                    
                    if subproblem >= 0: 
                        res = min(res, 1 + subproblem)
            
            cache[target] = res
            
            return res if res != math.inf else -1


        if not amount: return 0
        return f(amount)
