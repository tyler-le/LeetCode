class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
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
            