class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0 for _ in range(n+1)]

        for x in range(1, len(dp)):
            for i in range(1, x):
                if (x-i) <= 0: 
                    dp[i] = 0
                
                else: 
                    break_choice = i * dp[x-i]
                    dont_break_choice = i * (x-i)
                    dp[x] = max(dp[x], break_choice, dont_break_choice)

        return dp[n]

        cache = {}
        def f(x):
            if x <= 0: return 0
            if x in cache: return cache[x]

            res = 0
            for i in range(1, x):
                # here we split x into two parts: i and (x-i)
                res = max(res, i * f(x - i)) # break (x-i)
                res = max(res, i * (x - i)) # don't break (x-i)
            
            cache[x] = res
            return res
        
        return f(n)