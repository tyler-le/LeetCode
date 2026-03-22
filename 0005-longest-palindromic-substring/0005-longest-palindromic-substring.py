class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] returns True if s[i...j] is a palindrome
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]
        res = (1, 0, 0)

        # Base cases
        for i in range(n):
            for j in range(n):
                if i >= j: 
                    dp[i][j] = True
                    
        
        # Fill out the rest
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                
                if dp[i][j] and j-i+1 > res[0]:
                    res = (j-i+1, i, j)
        
        return s[res[1]: res[2]+1]



        """
        RECURSION + MEMOIZATION
        """
        # f(i, j) returns if s[i...j] is a palindrome
        # cache = {}

        # def f(i, j):
        #     if i >= j: return True
        #     if (i, j) in cache: return cache[(i, j)]
            
        #     res = False
        #     if s[i] == s[j]: res = f(i+1, j-1)
        #     else: res = False
            
        #     cache[(i, j)] = res
        #     return cache[(i, j)]

        # res = (0, -1, -1)
        # n = len(s)

        # for i in range(n):
        #     for j in range(i, n):
        #         if f(i, j) and (j-i+1 > res[0]):
        #             res = (j-i+1, i, j)
        
        # return s[res[1] : res[2] + 1]


            
          