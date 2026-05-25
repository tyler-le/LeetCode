class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        if obstacleGrid[n-1][m-1] == 1: return 0

        dp[n-1][m-1] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if obstacleGrid[i][j] == 1: continue
                if (i,j) == (n-1,m-1):continue

                down = dp[i+1][j] if i+1 < n else 0
                right = dp[i][j+1] if j+1 < m else 0
                dp[i][j] = down + right

        return dp[0][0]





        n, m = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def f(i, j):
            if i == n or j == m: return 0
            if obstacleGrid[i][j] == 1: return 0
            if i == n-1 and j == m-1: return 1

            res = 0

            # down
            res+=f(i+1, j)

            # right
            res+=f(i, j+1)

            return res

        return f(0,0)
