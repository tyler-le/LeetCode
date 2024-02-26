class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def convert_to_two(i, j):
            if i < 0 or j < 0 or i >= n or j >= m: return
            if grid[i][j] != 1: return
            
            grid[i][j] = 2
            q.append((i,j, 0))
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                convert_to_two(i+dx, j+dy)
        
        n, m = len(grid), len(grid[0])
        q = deque() # (row, col, steps)
        
        converted_island = False
        for i in range(n):
            if converted_island: break
            for j in range(m):
                if grid[i][j]:
                    convert_to_two(i, j)
                    converted_island = True
                    break
        
        while q:
            x, y, steps = q.popleft()
            
            for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                r, c = x+dx, y+dy
                if r < 0 or c < 0 or r >= n or c >= m: continue
                if grid[r][c] == 0: 
                    q.append((r,c,steps+1))
                    grid[r][c] = 2
                elif grid[r][c] == 1: return steps
                elif grid[r][c] == 2: continue
            

            
        
        