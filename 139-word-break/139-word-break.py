class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True
        
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i:i + len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
                if dp[i]: break # early exit
        return dp[0]