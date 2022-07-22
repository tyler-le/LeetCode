class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
    
        visited = set()

        def dfs(i,j, direction):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return ""

            if (i,j) in visited:
                return ""
                        
            visited.add((i,j))
            
            path = direction
            
            path += dfs(i-1,j, 'N')
            path += dfs(i,j+1, 'E')
            path += dfs(i+1,j, 'S')
            path += dfs(i,j-1, 'W')
            
            path += 'B'
            return path
        
        paths = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    paths.add(dfs(i,j, 'Start'))
        print(paths)
        return len(paths)