class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        FRESH, ROTTEN = 1, 2
        q, m, n = deque(), len(grid), len(grid[0])
        res, num_fresh = 0, 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN: q.append((i, j))
                if grid[i][j] == FRESH: num_fresh+=1
                    
        while q and num_fresh:
            res+=1
            num_rotten = len(q)
            
            for _ in range(num_rotten):
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    r = x+dx
                    c = y+dy
                    if r < 0 or c < 0 or r == m or c == n: continue
                    if grid[r][c] == FRESH: 
                        grid[r][c] = ROTTEN
                        num_fresh-=1
                        q.append((r,c))                    
            
        
        return res if num_fresh == 0 else -1
        
        
        