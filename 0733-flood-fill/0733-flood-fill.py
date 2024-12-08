class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.appendleft([sr, sc])
        initial_color = image[sr][sc]
        image[sr][sc] = color
        n, m = len(image), len(image[0])
        visited = set([(sr,sc)])
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r, c = x+dx, y+dy
                
                if r < 0 or c < 0 or r >= n or c >= m or image[r][c] != initial_color or (r,c) in visited:
                    continue

                q.appendleft([r, c])
                visited.add((r,c))
                image[r][c] = color
        
        return image
            