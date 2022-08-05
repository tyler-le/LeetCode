class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        ROWS = len(rooms)
        COLS = len(rooms[0])
        GATE, OBSTACLE, EMPTY = 0, -1, 2147483647
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == GATE:
                    q.append((i,j))
        
        while q:
            row, col = q.popleft()
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                if 0 <= r < ROWS and 0 <= c < COLS and rooms[r][c] == EMPTY:
                    rooms[r][c] = dist
                    q.append((r,c))