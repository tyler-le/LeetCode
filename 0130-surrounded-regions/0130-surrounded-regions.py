class Solution:
    def solve(self, board: List[List[str]]) -> None:

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m: return

            if board[x][y] != "O": return

            board[x][y] = "Z"

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(x + dx, y + dy)

        # loop border
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1) and board[i][j] == "O":
                    dfs(i,j)
                if (j == 0 or j == m-1) and board[i][j] == "O":
                    dfs(i,j)

        # mark all Os as X

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # mark all Z as O
        for i in range(n):
            for j in range(m):
                if board[i][j] == "Z":
                    board[i][j] = "O"