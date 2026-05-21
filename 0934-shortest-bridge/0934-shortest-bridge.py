class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        res = math.inf

        # change "1"-island to a "2"-island
        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m: return
            if grid[i][j] != 1: return
            grid[i][j] = 2
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = i + di
                c = j + dj
                dfs(r,c)

        def change_island():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        dfs(i,j)
                        return
            

        # first change an island to all 2s        
        change_island()

        # run multisource bfs from 1-nodes to 2-nodes
        q = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i,j,0))
                    visited.add((i,j))

        while q:
            level_size = len(q)
            for _ in range(level_size):
                popped_x, popped_y, popped_dist = q.popleft()

                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    r = popped_x + dx
                    c = popped_y + dy
                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if (r,c) in visited: continue
                    if grid[r][c] == 2: return popped_dist
                    visited.add((r,c))
                    q.append((r,c,popped_dist + 1))

    