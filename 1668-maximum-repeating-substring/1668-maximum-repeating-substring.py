class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        # dp[i] = max number of consecutive repeats that END at index i
        # so dp[i] = 1 + dp[i - len(word)]

        n, m = len(sequence), len(word)
        dp = [0 for _ in range(n+1)]

        for i in range(m, n+1):
            x = sequence[i-m:i]
            if x == word:
                dp[i] = 1 + dp[i-m] if i - m >= 0 else 1

        return max(dp)
