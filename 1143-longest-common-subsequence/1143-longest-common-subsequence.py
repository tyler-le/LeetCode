class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        """
        DP
        dp[i][j] = longest common sequence between text1[0:i] and text2[0:j]
        """

        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] += 1 + (
                        dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                    )
                else:
                    first = dp[i-1][j] if i-1 >= 0 else 0
                    second = dp[i][j-1] if j-1 >= 0 else 0
                    dp[i][j] += max(first, second)


        return dp[n-1][m-1]



        """
        RECURSION
        f(i,j) = longest common subsequence between text1[0:i] and text2[0:j]
        """
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


            
