class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = (1, [0,0])

        for substr_len in range(n):

            for i in range(n - substr_len):
                j = i + substr_len

                # base case: length 0,1 strings always true
                if j-i+1 <= 1: 
                    dp[i][j] = True
                    continue

                # base case: length 2 substrings just compare their chars
                # can't be found via dp[i+1][j-1] because j will be > than i
                elif j-i+1 == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True

                # recursive call: length 3+ substrings compare chars at the end 
                # AND check if the inner substring is a palindrome

                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                
                # update result
                if dp[i][j] and j-i+1 > res[0]: 
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


