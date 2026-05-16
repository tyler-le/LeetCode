class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)

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





            