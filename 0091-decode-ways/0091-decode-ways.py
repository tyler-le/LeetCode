class Solution:
    def numDecodings(self, s: str) -> int:
        # map i to number of ways to decode s[i:]
        dp = {len(s) : 1}

        def helper(i):
            # base case(s)
            if i in dp: return dp[i]
            if s[i] == "0": return 0
            
            # solve s[(i+1):]
            res = helper(i+1)
            
            # if we can group s[i] ++ s[i+1], then solve s[(i+2):]
            if (i+1 < len(s)) and ((s[i] == "1")
                or s[i] == "2" and  s[i+1] in "0123456"):
                res+=helper(i+2)
                dp[i] = res
            
            return res
        
        return helper(0)
                
                
        