class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def bfs(i, j):
            
            while q:
                x, y, dist = q.popleft()
                rooms[x][y] = dist if rooms[x][y] == 0 else min(rooms[x][y], dist)
                
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if x+dx < 0 or y+dy < 0 or x+dx >= n or y+dy >= m: continue   
                    if rooms[x+dx][y+dy] != EMPTY: continue
                    q.append((x+dx, y+dy, dist+1))
                    
        
        # for each gate, run bfs and update accordingly
        n, m, q = len(rooms), len(rooms[0]), deque()
        GATE, WALL, EMPTY = 0, -1, 2**31 - 1
        
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == GATE:
                    q.append((i, j, 0))
        
        bfs(i, j)
                    