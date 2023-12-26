class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
              
        rows, cols = len(heights), len(heights[0])
        visited = set()
        min_heap = [(0, 0, 0, 0)] # (max_diff, x, y, diff)
        
        while min_heap:
            max_diff, x, y, diff = heappop(min_heap)
            if (x,y) in visited: continue
            if (x,y) == (rows-1, cols-1): return max_diff
            visited.add((x,y))
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:                
                r, c = x+dx, y+dy
                if 0 <= r < rows and 0 <= c < cols: 
                    new_diff = abs(heights[r][c] - heights[x][y])
                    el = (max(max_diff, new_diff), r, c, new_diff)
                    heappush(min_heap, el)
        
                
        