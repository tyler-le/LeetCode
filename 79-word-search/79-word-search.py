class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def backtrack(r, c, index):
            if index == len(word): return True
            if r < 0 or c < 0 or r == ROWS or c == COLS: return False
            if (r,c) in visited: return False
            if board[r][c] != word[index]: return False
            
            
            visited.add((r,c))
            
            res = backtrack(r+1,c,index+1) \
                or backtrack(r-1,c,index+1) \
                or backtrack(r,c+1,index+1) \
                or backtrack(r,c-1,index+1)
            
            visited.remove((r,c))
            return res
        
        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0): 
                    return True
        return False