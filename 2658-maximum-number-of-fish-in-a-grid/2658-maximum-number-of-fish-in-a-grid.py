class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        def bfs(x, y):
            q = deque([(x,y)])
            num_fish = 0

            while q:
                popped_x, popped_y = q.popleft()
                num_fish+=grid[popped_x][popped_y]
                grid[popped_x][popped_y] = 0
                
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r = popped_x + dx
                    c = popped_y + dy

                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if grid[r][c] == 0: continue
                    q.append((r,c))
                    
                    


            return num_fish

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    res = max(res, bfs(i, j))

        return res