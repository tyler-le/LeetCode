class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = the longest common subsequence between t1[0...i] and t2[0...j]
        
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                
                if text1[i] == text2[j]: 
                    dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
                else: 
                    left = dp[i][j-1] if j > 0 else 0
                    up = dp[i-1][j] if i > 0 else 0
                    dp[i][j] = max(left, up)
        
        return dp[-1][-1]