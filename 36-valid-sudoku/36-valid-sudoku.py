class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # loop thru rows
        for i in range(len(board)):
            my_set = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in my_set:
                    return False
                my_set.add(board[i][j])

        # loop thru cols
        for i in range(len(board)):
            my_set = set()
            for j in range(len(board[0])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in my_set:
                    return False
                my_set.add(board[j][i])
                
        # loop 3x3 subgrid
        squares = {} # key is (row, col)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                if (i//3, j//3) not in squares:
                    squares[(i//3, j//3)] = set()
                if board[i][j] in squares[(i//3, j//3)]:
                    return False
                else:
                    squares[(i//3,j//3)].add(board[i][j])
                
        return True
                
                
            
                