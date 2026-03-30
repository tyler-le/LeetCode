class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m: return 1
            if grid[x][y] == 0: return 1
            if (x, y) in visited: return 0

            visited.add((x,y))

            res = 0
            res+=dfs(x+1, y)
            res+=dfs(x-1, y)
            res+=dfs(x, y+1)
            res+=dfs(x, y-1)
            return res

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return dfs(i, j)