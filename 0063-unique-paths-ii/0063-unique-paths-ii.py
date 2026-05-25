class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
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
