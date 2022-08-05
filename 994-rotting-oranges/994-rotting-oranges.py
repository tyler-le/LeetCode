class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS, fresh, time = len(grid), len(grid[0]), 0, 0
        q, visited = deque(), set()
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == FRESH: 
                    fresh+=1
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                    visited.add((i,j))

        while q and fresh:
            time+=1
            for _ in range(len(q)):
                x, y = q.popleft()
                
                for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
                    r, c = x + dx, y + dy
                    if r < 0 or c < 0 \
                        or r == ROWS or c == COLS \
                        or grid[r][c] != FRESH or (r,c) in visited:
                        continue
                        
                    grid[r][c] = ROTTEN
                    fresh-=1
                    q.append((r,c))
                    visited.add((r,c))
            
                
        return time if fresh == 0 else -1
                
        