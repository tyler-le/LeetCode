class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n, m, level = len(grid), len(grid[0]), 0       
        q, visited, res = deque(), set(), 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append((i, j, 0))
        
        if not q or n*m == len(q): return -1
        
        while q:
            x, y, d = q.popleft()
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = x+dx
                c = y+dy
                
                if r < 0 or c < 0 or r >= n or c >= m or (r,c) in visited or grid[r][c]:
                    continue
                    
                q.append((r,c, d+1))
                res = max(res, d+1)
                visited.add((r,c))
                
        return res
            
                    
        