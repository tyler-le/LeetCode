class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j, direction):

            nonlocal path

            if i < 0 or j < 0 or i == n or j == m:
                return
            if grid[i][j] == 0:
                return

            path.append(direction)
            grid[i][j] = 0

            # left
            dfs(i, j+1, "left")
            path.append("back")

            # down
            dfs(i+1, j, "down")
            path.append("back")

            # up
            dfs(i-1, j, "up")
            path.append("back")

            # right
            dfs(i, j-1, "right")
            path.append("back")
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, "start")
                    seen.add("".join(path))

        return len(seen)