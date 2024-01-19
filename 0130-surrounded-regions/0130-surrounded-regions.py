class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # navigate thru edges
        # for each "O" on the edge -> Change to "Y" and dfs
        
        # after all this, change all remaining "O's" to "X"
        # Change "Y" back to "O"
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m: return
            if (x,y) in visited: return
            if board[x][y] != "O": return
            
            board[x][y] = "Y"
            visited.add((x,y))
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x+dx, y+dy)
            
        
        n, m = len(board), len(board[0])
        visited = set()
        
        for c in range(m):
            if board[0][c] == "O": dfs(0, c)
            if board[n-1][c] == "O": dfs(n-1, c)
                
        for r in range(n):
            if board[r][0] == "O": dfs(r, 0)
            if board[r][m-1] == "O": dfs(r, m-1)
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O": board[i][j] = "X"
                elif board[i][j] == "Y": board[i][j] = "O"
        
        
        