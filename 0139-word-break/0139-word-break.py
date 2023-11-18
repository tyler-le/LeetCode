class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        
        for i in range(n+1):
            for w in wordDict:
                if (i - len(w) >= 0) and (dp[i - len(w)]) and (s[i-len(w):i] == w):
                    dp[i] = True
                    
        return dp[-1]
            