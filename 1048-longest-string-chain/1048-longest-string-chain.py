class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        
        words.sort(key = lambda x : len(x))
        
        for word in words:
            dp[word] = 1
            
            for i in range(len(word)):
                
                # word minus the ith character
                prev = word[:i] + word[i+1:]
                
                if prev in dp:
                    dp[word] = max(dp[word], 1 + dp[prev])
                    
        return max(dp.values())
                    