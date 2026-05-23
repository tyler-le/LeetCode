class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        required = 0
        n, m = len(grid), len(grid[0])
        WALL, EMPTY, START, END = [-1, 0, 1, 2]
        start, end = (), ()
        res = 0
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == EMPTY:
                    required+=1
                elif grid[i][j] == START:
                    start = (i,j)
                    required+=1
                elif grid[i][j] == END:
                    end = (i,j)
                    required+=1

        def backtrack(x, y, path_len, path):
            nonlocal res, visited

            if (x,y) == end:
                # print(f"found end with path = {path} and path_len = {path_len}")
                if path_len == required: res+=1
                return

            if (x,y) in visited: return
            visited.add((x,y))
            path.append((x,y))

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r, c = x + dx, y + dy
                if r < 0 or c < 0 or r >= n or c >= m: continue
                if grid[r][c] == WALL: continue
                backtrack(r, c, path_len + 1, path)

            visited.remove((x,y))
            path.pop()

        backtrack(start[0], start[1], 1, [])
        return res


        