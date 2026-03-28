from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        
        
        def is_perfect_square(x):
            return sqrt(x).is_integer()

        """
        DP
        dp[i] = the least number of perfect squares to sum to i
        hence dp[i] = dp[i - j] for all perfect squares j
        """
        dp = [math.inf for _ in range(n+1)]
        perfect_squares = [x for x in range(n+1) if is_perfect_square(x)]

        for i in range(len(dp)):
            if is_perfect_square(i): 
                dp[i] = 1
        
        for i in range(len(dp)):
            for j in perfect_squares:
                if j > i: break
                dp[i] = min(dp[i], 1 + dp[i-j])
        
        return dp[n]
        
        """
        RECURSION + MEMOIZATION
        f(x)  = the least number of perfect squares that sum to x
        hence f(x) = f(x - y) for all perfect squares y
        """
        cache = {}
        def f(x) -> int:
            res = math.inf

            if x <= 0: return math.inf
            if is_perfect_square(x): return 1

            if x in cache: return cache[x]
        
            for y in range(1, x):
                if is_perfect_square(y):
                    res = min(res, 1 + f(x-y))
            
            cache[x] = res
            return res


        
        return f(n)