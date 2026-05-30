class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        q = deque()
        visited = set()
        grid = [[0 for _ in range(m)] for _ in range(n)]

        for i, j, color in sources:
            grid[i][j] = color
            if grid[i][j] > 0:
                    q.append((i, j))
                    visited.add((i,j))

        while q:
            level_size = len(q)
            level_visited = set()

            for _ in range(level_size):
                popped_x, popped_y = q.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r = popped_x + dx
                    c = popped_y + dy

                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if (r,c) in visited: continue
                    grid[r][c] = max(grid[r][c], grid[popped_x][popped_y])
                    level_visited.add((r,c))

            for x, y in level_visited:
                q.append((x,y))
                visited.add((x,y))
                
        
        return grid
                    
                    
