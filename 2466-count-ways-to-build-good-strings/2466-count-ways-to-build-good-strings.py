class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        # dp[i] = number of ways to build a happy string of length i
        dp = [0 for _ in range(high+1)]
        n = len(dp)
        res = 0
        
        MOD = 10**9 + 7
        dp[zero] += 1
        dp[one] += 1
        
        for i in range(n):
            x = dp[i-zero] if (i-zero) >= 0 else 0
            y = dp[i-one] if (i-one) >= 0 else 0
            dp[i] += (x+y) % MOD
            
        for i in range(low, high+1):
            res = (res + dp[i]) % MOD
        
        return res