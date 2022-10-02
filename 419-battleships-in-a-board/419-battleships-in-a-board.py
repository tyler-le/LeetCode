class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        #visited = set()
        
        def dfs(i,j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]): return
            if board[i][j] == '.': return
            #visited.add((i,j))
            board[i][j] = '.'
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    res+=1
                    dfs(i, j)
        return res
        