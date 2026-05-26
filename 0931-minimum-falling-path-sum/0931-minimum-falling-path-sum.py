class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n, m = len(matrix), len(matrix[0])
        dp = [[math.inf for _ in range(m)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1: 
                    dp[i][j] = matrix[i][j]
                    continue
                
                score = matrix[i][j]
                left = dp[i+1][j-1] if j-1 >= 0 else math.inf
                under = dp[i+1][j] if i+1 < n else math.inf
                right = dp[i+1][j+1] if i+1 < n and j+1 < m else math.inf
                score+=min(left, under, right)
                dp[i][j] = score

        return min(dp[0])



        n, m = len(matrix), len(matrix[0])
        res = math.inf

        @cache
        def f(i, j):
            if j < 0 or j >= m: 
                return math.inf
            if i == n-1:
                return matrix[i][j]

            score = matrix[i][j]
            left = f(i+1, j-1)
            under = f(i+1, j)
            right = f(i+1, j+1)
            score += min(left, under, right)

            return score

        for col in range(len(matrix[0])):
            num = matrix[0][col]

            choice = f(0, col)
            res = min(choice, res)
        
        return res
            