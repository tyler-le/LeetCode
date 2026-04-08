class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        """
        DP (translated from recursive method)
        filling bottom-right to top-left
        """
        n, m = len(word1), len(word2)
        dp = [[math.inf for _ in range(m+1)] for _ in range(n+1)]

        # exhausted word1 but not word2
        for j in range(m+1):
            dp[n][j] = m-j
        
        # exhausted word2 but not word1
        for i in range(n+1):
            dp[i][m] = n - i

        # exhausted both words
        dp[n][m] = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j] 
                    replace = 1 + dp[i+1][j+1]  
                    dp[i][j] = min(insert, delete, replace)
        
        return dp[0][0]



        """
        RECURSIVE + MEMOIZATION
        - Insert → Add a char to word1 to match word2[j], advance j but not i (since we inserted before i)
        - Delete → Remove word1[i], advance i but not j (since we have not matched j yet)
        - Replace → word1[i] becomes word2[j], advance both since they match now
        """
        
        n, m = len(word1), len(word2)
        cache = {}        
        def f(i, j):

            # exhaust word1, can only perform inserts to get to word2
            if i == n and j < m:
                return m - j
            
            # exhaust word2, can only perform deletes to get to word2
            if j == m and i < n:
                return n - i

            # reached the end on both words
            if i == n and j == m:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]

            res = math.inf

            if word1[i] == word2[j]:
                res = 0 + f(i+1, j+1)
            else:
                insert = 1 + f(i, j+1)
                delete = 1 + f(i+1, j)
                replace = 1 + f(i+1, j+1)
                res = min(insert, delete, replace)
            
            cache[(i,j)] = res
            return res

        return f(0, 0)
