class Solution:
    def numDecodings(self, s: str) -> int:
        
        """
        DP SOLUTION
        """
        # dp[i] = num ways to break s[i:]
        # return dp[0]

        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1

        for i in range(n-1, -1, -1):

            take_first = int(s[i])
            if 1 <= take_first <= 26:
                dp[i]+=dp[i+1]

            take_first_two = int(s[i:i+2])
            if i+2 <= n and 10 <= take_first_two <= 26:
                dp[i]+=dp[i+2]

        return dp[0]

        """
        RECURSION + MEMOIZATION
        """
        # cache = {}
        # # f(x) is the number of ways to decode x
        # def f(x):

        #     # base case(s) - x turns into empty string or singleton
        #     if not x: return 1
        #     if len(x) == 1: 
        #         if x == "0": return 0 # invalid so return 0
        #         else: return 1 # singleton is between 1-9, which means it has one valid encoding

        #     res = 0
        #     if x in cache: return cache[x]

        #     # take x[0] and recurse on x[1:]
        #     # don't recurse on x[0], since we want to break the 'rest' part of the string 
        #     # and dwindle it down to the base case
        #     first, rest = x[0], x[1:]
        #     if 1 <= int(first) <= 26 and not (len(first) == 2 and first[0] == "0"): 
        #         res += f(rest)

        #     # take x[0:2] and recurse on x[2:] 
        #     # don't recurse on x[0], since we want to break the 'rest' part of the string 
        #     # and dwindle it down to the base case    
        #     first, rest = x[0:2], x[2:]   
        #     if 1 <= int(first) <= 26 and not (len(first) == 2 and first[0] == "0"): 
        #         res += f(rest)

        #     cache[x] = res
        #     return res    
        
        # return f(s)
