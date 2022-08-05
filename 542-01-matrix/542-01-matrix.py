class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q, visited = deque(), set()
        ROWS, COLS = len(mat), len(mat[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            x, y = q.popleft()
            
            for dx, dy in (-1, 0), (1,0), (0,1), (0,-1):
                r = x + dx
                c = y + dy
                
                if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited:
                    continue
                
                mat[r][c] = 1 + mat[x][y]
                q.append((r,c))
                visited.add((r,c))
        
        return mat