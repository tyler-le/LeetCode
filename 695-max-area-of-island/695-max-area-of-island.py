class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def bfs(i,j):
            q, area = deque(), 1
            q.append((i,j))
            visited.add((i,j))

            while q:
                x, y = q.popleft()
                
                for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
                    r, c = x+dx, y+dy
                    if r < 0 or c < 0 \
                        or r == ROWS or c == COLS \
                        or grid[r][c] == 0 or (r,c) in visited:
                        continue
                        
                    area+=1
                    q.append((r,c))
                    visited.add((r,c))
                    
            return area
                    

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res = max(bfs(i,j), res)
                    
        return res