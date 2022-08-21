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
            # we found the word
            if index == len(word): return True
            
            # out of bounds
            if r < 0 or c < 0 or r == ROWS or c == COLS: return False
            
            # cannot revisit
            if (r,c) in visited: return False
            
            # the current position in the board is not the correct char
            if board[r][c] != word[index]: return False
            
            # mark current cell as visited
            visited.add((r,c))
            
            # visit all neighbors
            res = backtrack(r+1,c,index+1) \
                or backtrack(r-1,c,index+1) \
                or backtrack(r,c+1,index+1) \
                or backtrack(r,c-1,index+1)
            
            # unvisit neighbor
            visited.remove((r,c))
            
            # if we ever returned true, then we found the word
            return res
        
        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0): 
                    return True
        return False