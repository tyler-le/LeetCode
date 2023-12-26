class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        def dfs(x, y):
            if x < 0 or y < 0: return
            if x >= rows or y >= cols: return
            if grid[x][y] != 1: return
            
            grid[x][y] = 2
            q.append((x,y,0))
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r, c = x+dx, y+dy
                dfs(r, c)
        
        # find one island
        for r in range(rows):
            found = False
            for c in range(cols):
                # change it to all 2's
                if grid[r][c] == 1: 
                    dfs(r,c)
                    found = True
                    break
            if found: break
                    
                    
        # then for all 2's, find the shortest path to the second island (1's)
        while q:
            x, y, steps = q.popleft()
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= x+dx < rows and 0 <= y+dy < cols:
                    if grid[x+dx][y+dy] == 0:
                        q.append((x+dx, y+dy, steps+1))
                        grid[x+dx][y+dy] = 2
                    elif grid[x+dx][y+dy] == 1: return steps
                    elif grid[x+dx][y+dy] == 2: continue
                    

        
        
        
        
        
            
                                
        