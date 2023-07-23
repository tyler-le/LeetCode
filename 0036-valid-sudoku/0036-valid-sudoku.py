class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        subgrids = collections.defaultdict(set)
        
        
        for r in range (len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".": continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in subgrids[(r//3, c//3)]: 
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subgrids[(r//3, c//3)].add(board[r][c])
                
        return True
    
                