class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # go through the borders, if 'O', run dfs on it and mark it and all 'O' nbors as 'T'
        # then double for-loop and change all 'O' to 'X' and all 'T' to 'O'
        def dfs(i,j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] != 'O':
                return
            if board[i][j] == 'O':
                board[i][j] = 'T'
                
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                on_border = (i == 0) or (i == len(board) - 1) or (j == 0) or (j == len(board[0]) - 1)
                if on_border and board[i][j] == 'O': dfs(i,j)
                    
        print (board)        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'T': board[i][j] = 'O'
                    
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == 'T': board[i][j] = 'O'
      