class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        visited = set()
        n, m = len(board), len(board[0])
        
        def dfs(r, c):
            if (r, c) in visited: return
            if r < 0 or c < 0 or r >= n or c >= m: return
            if board[r][c] == "X": return
            
            if board[r][c] == "O": board[r][c] = "T"
            visited.add((r,c))
                
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + i, c + j)
                
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and ((i == 0) or (i == n-1) or (j == 0) or (j == m-1)): 
                    dfs(i, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"
                    
                
                