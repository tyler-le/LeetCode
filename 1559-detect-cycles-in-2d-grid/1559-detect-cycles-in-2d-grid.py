class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        n, m = len(grid), len(grid[0])

        def has_cycle(x, y, prev):
            if (x, y) in visited: return True

            visited.add((x,y))
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = x + dx
                c = y + dy

                if r < 0 or c < 0 or r >= n or c >= m: continue
                if prev and (r,c) == prev: continue
                if grid[r][c] != grid[x][y]: continue

                if has_cycle(r, c, (x,y)): return True


        for i in range(n):
            for j in range(m):
                if (i, j) in visited: continue
                if has_cycle(i, j, None): 
                    return True
        
        return False