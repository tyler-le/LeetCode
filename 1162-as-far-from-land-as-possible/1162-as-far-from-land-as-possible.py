class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        n, m = len(grid), len(grid[0])
        res = -1

        for i in range(n): 
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i,j,0))
                    visited.add((i,j))

        while q:
            level_size = len(q)

            for _ in range(level_size):
                popped_x, popped_y, popped_dist = q.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r = popped_x + dx
                    c = popped_y + dy

                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if (r,c) in visited: continue
                    if grid[r][c] != 0: continue
                    res = max(res, popped_dist + 1)
                    q.append((r,c,popped_dist+1))
                    visited.add((r,c))

        return res