class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        n, m = len(grid), len(grid[0])
        q = deque()
        res, num_fresh = 0, 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == ROTTEN: q.append((i,j))
                if grid[i][j] == FRESH: num_fresh+=1
                    
        while q and num_fresh:
            res+=1 
            level_size = len(q)
            
            for _ in range(level_size):
                x, y = q.popleft()
                
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r, c = x + dx, y + dy
                    
                    if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] != FRESH: continue
                    
                    grid[r][c] = ROTTEN
                    num_fresh-=1
                    q.append((r,c))
            
            
        return res if not num_fresh else -1