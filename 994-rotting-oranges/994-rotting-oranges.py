class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows, cols, q, visited = len(grid), len(grid[0]), deque(), set()
        fresh, time = 0, 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    visited.add((i,j))
                    q.append((i,j))
        while q and fresh:
            # process current level of neighbors
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if x+dx < 0 or y+dy < 0 \
                        or x+dx == rows or y+dy == cols \
                        or grid[x+dx][y+dy] != 1:
                        continue
                        
                    grid[x+dx][y+dy] = 2
                    q.append((x+dx, y+dy))
                    fresh-=1
            time+=1

    
                
        return time if fresh == 0 else -1
                    
            
                