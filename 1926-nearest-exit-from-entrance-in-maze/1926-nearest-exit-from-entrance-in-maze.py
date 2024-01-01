class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        q = deque([(entrance[0], entrance[1], 0)])
        n, m = len(maze), len(maze[0])
        WALL, EMPTY = "+", "."
        visited = set()
        
        while q:    
            

            x, y, steps = q.popleft()
            
            if (x,y) in visited: continue
            if (x == 0 or x == n-1 or y == 0 or y == m-1) and (x,y) != tuple(entrance):
                return steps
                
            visited.add((x,y))

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = x + dx
                c = y + dy
                
                if r < 0 or c < 0 or r >= n or c >= m: continue
                elif maze[r][c] == WALL: continue
                else:
                    q.append((r, c, steps + 1))
                    
        
        return -1