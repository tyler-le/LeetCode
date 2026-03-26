class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        """
        DP
        """
        # dp[i] = dp[0:i] inclusive is word breakable

        # return dp[n]

        n = len(s)
        dp = [False for _ in range(n)]

        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n:
                    prefix = s[i : i+len(word)]

                    if prefix in wordDict:
                        if i + len(word) >= len(dp):
                            dp[i] = True
                        elif dp[i + len(word)]:
                            dp[i] = True

        
        
        
        return dp[0]






        """
        RECURSION + MEMOIZATION
        """
        cache = {}
        def f(x):
            if x == "": return True
            if x in cache: return cache[x]

            for word in wordDict:
                prefix = x[:len(word)]
                if prefix == word and f(x[len(word):]):
                    cache[x] = True
                    return True
            cache[x] = False
            return False
        
        return f(s)