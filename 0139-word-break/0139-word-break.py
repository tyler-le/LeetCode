class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[-1] = True
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                m = len(word)
                if s[i:i+m] == word and dp[i+m]:
                    dp[i] = True
                    break
        return dp[0]