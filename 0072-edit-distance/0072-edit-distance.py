class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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
