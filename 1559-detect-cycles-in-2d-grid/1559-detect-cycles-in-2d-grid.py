class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        n, m = len(grid), len(grid[0])

        def has_cycle(x, y, parent):
            if (x,y) in visited: return True
            visited.add((x,y))

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = x + dx
                c = y + dy

                if r < 0 or c < 0 or r >= n or c >= m: continue
                if grid[x][y] != grid[r][c]: continue
                if (r,c) == parent: continue
                if has_cycle(r,c, (x,y)): return True
            
            return False

        for i in range(n):
            for j in range(m):
                if (i, j) in visited: continue
                if has_cycle(i,j, None): return True


        return False