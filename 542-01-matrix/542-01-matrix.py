class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS, visited, q = len(mat), len(mat[0]), set(), deque()
        
        for i in range (ROWS):
            for j in range (COLS):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            x, y = q.popleft()
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x+direction[0], y+direction[1]
                if new_x < 0 or new_y < 0 \
                    or new_x == ROWS or new_y == COLS \
                    or (new_x, new_y) in visited:
                    continue
                mat[new_x][new_y] = mat[x][y]+1
                q.append((new_x, new_y))
                visited.add((new_x, new_y))
                
        return mat
                
            