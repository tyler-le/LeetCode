class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [0 for _ in range(n+1)]

        for i in range(m, n+1):
            x = sequence[i-m:i]
            
            if x == word:
                dp[i] = 1 + dp[i-m] 

        return max(dp)