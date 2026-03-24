class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]
        res = 0

        for i in range(n):
            for j in range(n):
                if i >= j:
                    if i == j: res+=1
                    dp[i][j] = True
        
        for length in range(2, n+1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res+=1
                
        
        return res
                
    


        """
        RECURSION + MEMOIZATION
        """
        # "is s[i...j] a palindrome?"
        # cache = {}
        # def f(i, j):
        #     if i >= j: return True
        #     if (i, j) in cache: return cache[i, j]

        #     inner_res = f(i+1, j-1)

        #     if s[i] == s[j] and inner_res: 
        #         cache[(i, j)] = True
        #         return True

        #     cache[(i, j)] = False
        #     return False

        # n = len(s)
        # res = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         if f(i, j):
        #             res+=1
        
        # return res