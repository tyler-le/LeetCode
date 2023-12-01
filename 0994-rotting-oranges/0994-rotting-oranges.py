class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, time = deque(), 0
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == FRESH: 
                    num_fresh+=1
                
                if grid[row][col] == ROTTEN:
                    q.append((row, col))
        
                    
        while q and num_fresh:
            time+=1
            level_size = len(q)

            for _ in range(level_size):
                x, y = q.popleft()
                
                for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (x+r < 0) or (x+r >= m) \
                    or (y+c < 0) or (y+c >= n) \
                    or (grid[x+r][y+c] != FRESH): 
                        continue
                    
                    
                    grid[x+r][y+c] = ROTTEN
                    num_fresh-=1
                    q.append((x+r, y+c))
            

                
                
        return -1 if (num_fresh) else time
        
                