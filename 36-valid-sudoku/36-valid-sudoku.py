class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # check rows
        digits = set()
        for row in board:
            digits = set()
            for r in row:
                if r == '.': continue
                elif r in digits: return False
                else: digits.add(r)
        
        # check cols
        for col in range(len(board[0])):
            digits = set()
            for row in range(len(board)):
                if board[row][col] == '.': continue
                elif board[row][col] in digits: return False
                else: digits.add(board[row][col])
        
        # check 3x3 subgrid
        subgrid = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                digit = board[i][j]
                if digit == '.': continue
                elif digit in subgrid[(i//3, j//3)]: return False
                else: subgrid[(i//3, j//3)].add(digit)
        
        return True
                    
        
                