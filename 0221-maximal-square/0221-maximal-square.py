class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        res = 0
        n, m = len(matrix), len(matrix[0])

        @cache
        def f(i, j):

            if i < 0 or j < 0 or i >= n or j >= m: return 0
            if matrix[i][j] == "0": return 0

            up = f(i-1, j)
            left = f(i, j-1)
            diag = f(i-1, j-1)

            subproblem = min(up, left, diag)
            return 1 + subproblem


        for i in range(n):
            for j in range(m):
                res = max(res, f(i,j))

        return res**2