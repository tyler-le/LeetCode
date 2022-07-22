class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
                
            if grid[i][j] == 1 or (i,j) in visited:
                return True
            
            visited.add((i,j))
            is_closed = True
            
            is_closed &= dfs(i+1,j)  
            is_closed &= dfs(i-1,j) 
            is_closed &= dfs(i,j+1) 
            is_closed &= dfs(i,j-1)
            return is_closed
            
        
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 0 and (i,j) not in visited:
                    if dfs(i,j):
                        res += 1
        return res