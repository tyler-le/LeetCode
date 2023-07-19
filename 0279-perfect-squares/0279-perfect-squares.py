class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        
        def helper(num):
            ret = []
            for i in range(1, num+1):
                if sqrt(i) == int(sqrt(i)):
                    ret.append(i)
            return ret

        for i in range(2, n+1):
            square = 1
            while square*square <= i:            
                dp[i] = min(dp[i - square*square] + 1, dp[i])
                square+=1

        return dp[n]
            
            
        