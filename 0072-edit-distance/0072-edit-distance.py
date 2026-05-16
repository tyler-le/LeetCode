class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)
        dp = [[math.inf for _ in range(m+1)] for _ in range(n+1)]
        n, m = len(word1), len(word2)


        for i in range(n+1):
            dp[i][0] = i
            

        for j in range(m+1):
            dp[0][j] = j
            


        for i in range(1, n+1):
            for j in range(1, m+1):    
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]
                    dp[i][j] = min(dp[i][j], insert, delete, replace)

        return dp[n][m]


        @cache
        def f(i, j):
            # base case
            if i == n and j == m: return 0
            if i == n and j < m: return m - j 
            if i < n and j == m: return n - i
            
            res = math.inf

            # recurrence
            if word1[i] == word2[j]: 
                res = min(res, f(i+1, j+1))
            else:
                insert = 1 + f(i, j+1)
                delete = 1 + f(i+1, j)
                replace = 1 + f(i+1, j+1)
                res = min(res, insert, replace, delete)

            return res
        
        return f(0,0)





            