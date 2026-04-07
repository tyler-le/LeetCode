class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        visited = set()

        def bfs(x, y):
            q = deque([(x,y)])
            area = 1
            visited.add((x,y))

            while q: 
                popped_x, popped_y = q.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r = popped_x + dx
                    c = popped_y + dy

                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if (r,c) in visited: continue
                    if not grid[r][c]: continue
                    visited.add((r,c))
                    q.append((r,c))
                    area+=1
                    

            return area






        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i,j) not in visited:
                    print(i,j)
                    res = max(res, bfs(i, j))
                    print(res)

        return res