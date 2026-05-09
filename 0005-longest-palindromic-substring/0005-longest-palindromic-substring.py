class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        res = (1, [0,0])

        for substr_len in range(n):

            for i in range(n - substr_len):
                j = i + substr_len
                if i == j: 
                    dp[i][j] = True
                    continue

                if j-i+1 == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        if j-i+1 > res[0]: 
                            res = (j-i+1, (i,j))
                
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 > res[0]: 
                        res = (j-i+1, (i,j))

        start, end = res[1]
        return s[start: end+1]

                




        """
        n = len(s)
        res = (1, [0,0])
        cache = {}


        def f(i, j):
            nonlocal res

            if (i, j) in cache: 
                return cache[(i,j)]

            if i >= j: 
                cache[(i,j)] = True
                return cache[(i,j)]

            if s[i] == s[j] and f(i+1, j-1):
                if j-i+1 > res[0]: res = (j-i+1, (i,j))
                cache[(i,j)] = True
                return cache[(i,j)]
            
            cache[(i,j)] = False
            return cache[(i,j)]


        for i in range(n):
            for j in range(i, n):
                f(i, j)

        start, end = res[1]
        return s[start: end+1]
        """


