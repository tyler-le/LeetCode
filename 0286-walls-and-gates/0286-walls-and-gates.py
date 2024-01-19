class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def bfs(i, j):
            q = deque([(i, j, 0)])
            visited = set()
            
            while q:
                x, y, dist = q.popleft()
                rooms[x][y] = dist if rooms[x][y] == 0 else min(rooms[x][y], dist)
                
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if x+dx < 0 or y+dy < 0 or x+dx >= n or y+dy >= m: continue   
                    if rooms[x+dx][y+dy] == WALL: continue
                    if rooms[x+dx][y+dy] == GATE: continue
                    if (x+dx, y+dy) in visited: continue
                    q.append((x+dx, y+dy, dist+1))
                    visited.add((x+dx, y+dy))
                    
        
        # for each gate, run bfs and update accordingly
        n, m = len(rooms), len(rooms[0])
        GATE, WALL, EMPTY = 0, -1, 2**31 - 1
        
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == GATE:
                    bfs(i, j)
                    