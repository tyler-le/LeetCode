class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0
        memo = [[-1 for x in text2] for y in text1]
        
        
        def helper(i, j):
            if i >= len(text1) or j >= len(text2): 
                return 0
            
            if memo[i][j] != -1: return memo[i][j]
            
            if text1[i] == text2[j]: 
                #return max(res, helper(i+1, j+1) + 1)
                memo[i][j] = max(memo[i][j], helper(i+1, j+1) + 1)
            else:
                #return max(helper(i, j+1), helper(i+1, j))
                memo[i][j] = max(helper(i, j+1), helper(i+1, j))
                
            return memo[i][j]
            
        return helper(0, 0)