class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordSet:
                m = len(word)
                if i >= m and s[i-m:i] == word and dp[i-m]:
                    dp[i] = True
                    break
                    
        return dp[n]