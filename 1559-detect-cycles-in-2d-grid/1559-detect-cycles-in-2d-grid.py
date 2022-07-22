class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def dfs(i, j, char, prev):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != char:
                return False
            
            if (i,j) in visited: return True
            
            visited.add((i,j))

            if (i+1,j) != prev and dfs(i+1,j, char, (i,j)): return True
            if (i-1,j) != prev and dfs(i-1,j, char, (i,j)): return True
            if (i,j+1) != prev and dfs(i, j+1, char, (i,j)): return True
            if (i,j-1) != prev and dfs(i, j-1, char, (i,j)): return True
            
            return False
        
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited: continue
                if dfs(i,j, grid[i][j], (i,j)): return True
                
        return False
            
