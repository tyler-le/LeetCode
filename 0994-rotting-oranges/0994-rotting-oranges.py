class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # init vars
        n, m, q = len(grid), len(grid[0]), deque()
        num_fresh, res = 0, 0
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        
        
        for i in range(n):
            for j in range(m):
                # get total number of oranges
                if grid[i][j] == FRESH: num_fresh+=1
                # get all oranges that are initially rotten
                if grid[i][j] == ROTTEN: q.append((i,j))
        
        
        
        # run multisource bfs 
        while q and num_fresh:
            level_size = len(q)
            for _ in range(level_size):
                x,y = q.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r, c = x+dx, y+dy
                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if grid[r][c] != FRESH: continue
                    grid[r][c] = ROTTEN
                    num_fresh-=1
                    q.append((r,c))
            res+=1

        return res if not num_fresh else -1
                
            
        
        