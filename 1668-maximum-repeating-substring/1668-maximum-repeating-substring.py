class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        n, m = len(sequence), len(word)
        dp = [0 for _ in range(n+1)]

        for i in range(n+1):
            x = sequence[i-m:i]
            if not x: continue
            if x == word:
                if i - m >= 0:
                    dp[i] = 1 + dp[i-m]
                else:
                    dp[i] = 1

        
        return max(dp)
