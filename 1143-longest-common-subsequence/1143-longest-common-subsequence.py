class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = the longest common subsequence between t1[0...i] and t2[0...j]
        
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]: 
                    dp[i][j] = 1 + dp[i-1][j-1]
                else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp)
        return dp[-1][-1]