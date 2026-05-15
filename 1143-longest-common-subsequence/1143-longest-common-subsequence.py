class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m = len(text1), len(text2)

        @cache
        def f(i, j):
            res = 0
            if i == n or j == m: 
                return res

            if text1[i] == text2[j]:
                res += 1 + f(i+1, j+1)
            else:
                choice = max(f(i+1, j),f(i, j+1))
                res+=choice
            
            return res
        
        return f(0,0)


            
