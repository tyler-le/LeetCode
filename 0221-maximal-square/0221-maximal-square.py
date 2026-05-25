class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        res = 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0": 
                    dp[i][j] = 0
                    continue

                up = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0
                diag = dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0

                subproblem = min(up, left, diag)
                dp[i][j] = 1 + subproblem
                res = max(res, dp[i][j])

        return res**2


        """
        f(i,j) = the side length of the maximal square with (i,j) in the bottom right corner

        So if matrix[i][j] == "1", then we look at the squares formed from up, left, diag. 
        We can form a new square based off the minimum of these 3 results. 
        """
        
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