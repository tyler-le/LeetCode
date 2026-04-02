class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        visited = set()
        n, m = len(grid), len(grid[0])
        res = set()
        
        def dfs(x, y, path, direction):
            if x < 0 or y < 0 or x >= n or y >= m: return 
            if (x,y) in visited: return 
            if grid[x][y] == 0: return 

            visited.add((x,y))
            if direction: path.append(f"{direction} ")
            else: path.append("Start ")

            dfs(x, y-1, path, "Left")
            dfs(x, y+1, path, "Right")
            dfs(x-1, y, path, "Up")
            dfs(x+1, y, path, "Down")

            path.append("Backtracking")
            return path

        for i in range(n):
            for j in range(m):
                path = dfs(i, j, [], None)
                if path: res.add(tuple(path))
        
        return len(res)
        

