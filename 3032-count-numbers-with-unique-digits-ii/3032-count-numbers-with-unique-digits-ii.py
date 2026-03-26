class Solution:
    def numberCount(self, a: int, b: int) -> int:
        
        """
        DP
        """
        # dp[i] means numbers [0...i] has unique digits
        dp = [0 for _ in range(b+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, b+1):
            s = str(i)

            dp[i]+=dp[i-1]
            if (len(set(s)) == len(s)):
                dp[i]+=1
        
        return dp[b] - dp[a-1]



        """
        RECURSIVE + MEMOIZATION
        """
        # f(a,b) = f(b) - f(a-1)
        cache = {}
        def f(x):
            if x == 0: return 0
            if x == 1: return 1
            if x in cache: return cache[x]

            res = 0
            s = str(x)

            res += f(x-1) + (len(set(s)) == len(s))
            cache[x] = res

            return res
        
        return f(b) - f(a-1)

    

