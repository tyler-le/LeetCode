class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        ROWS, COLS, matching_color = len(image), len(image[0]), image[sr][sc]
        q, visited = deque(), set()
        
        q.append((sr, sc))
        visited.add((sr, sc))
        
        image[sr][sc] = color
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
                r, c = x+dx, y+dy
                if r < 0 or c < 0 \
                    or r == ROWS or c == COLS \
                    or image[r][c] != matching_color or (r,c) in visited:
                    continue
                    
                image[r][c] = color
                q.append((r,c))
                visited.add((r,c))
                
        return image
                
                
                
                
                
            
            