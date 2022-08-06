class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        q, visited = deque(), set()
        ROWS, COLS = len(rooms), len(rooms[0])
        WALL, GATE, EMPTY = -1, 0, 2147483647
        
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == GATE:
                    q.append((i,j))
                    visited.add((i,j))
                    
        while q:
            x,y = q.popleft()
            dist = rooms[x][y] + 1
            for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
                r, c = x+dx, y+dy
                
                if r < 0 or c < 0 \
                or r == ROWS or c == COLS \
                or rooms[r][c] != EMPTY or (r,c) in visited:
                    continue
                
                rooms[r][c] = dist
                q.append((r,c))
                visited.add((r,c))