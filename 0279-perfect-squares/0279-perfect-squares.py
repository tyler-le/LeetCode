from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        
        
        def is_perfect_square(x):
            return sqrt(x).is_integer()

        """
        DP
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
        """
        cache = {}
        def f(x) -> int:
            res = math.inf

            if x <= 0: return math.inf
            if is_perfect_square(x): return 1

            if x in cache: return cache[x]
        
            for num in range(1, x):
                if is_perfect_square(num):
                    res = min(res, 1 + f(x-num))
            
            cache[x] = res
            return res


        
        return f(n)