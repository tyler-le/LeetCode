class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        def dfs(x, y):
            
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            if (x,y) in visited: return 0
            visited.add((x,y))
            
            up = dfs(x-1,y)
            down = dfs(x+1,y)
            left = dfs(x,y-1)
            right = dfs(x,y+1)
            
            visited.remove((x,y))
            
            return grid[x][y] + max(up, down, left, right)
            
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                visited = set()
                res = max(res, dfs(r,c))
        return res