class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q, visited = deque(), set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0: 
                    q.append((i,j))
                    visited.add((i,j))
                
        while q:
            i, j = q.popleft()
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = i + x, j + y

                if new_x < 0 or new_y < 0 \
                    or new_x == len(mat) or new_y == len(mat[0]) \
                    or (new_x, new_y) in visited:
                    continue

                mat[new_x][new_y] = 1 + mat[i][j]
                q.append((new_x, new_y))
                visited.add((new_x, new_y))
        return mat
                    
                    
                    
                        