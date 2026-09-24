class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # multisource BFS

        q = deque() # (i, j, dist)
        n, m = len(rooms), len(rooms[0])
        WALL, GATE, EMPTY = -1, 0, 2**31 - 1

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == GATE:
                    q.append((i, j, 0))
        
        while q:
            level_size = len(q)
            for _ in range(level_size):
                popped_x, popped_y, popped_dist = q.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r = popped_x + dx
                    c = popped_y + dy

                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    if rooms[r][c] == EMPTY:
                        rooms[r][c] = popped_dist + 1
                        q.append((r, c, popped_dist + 1))


                

                

