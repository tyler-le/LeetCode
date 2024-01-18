class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(r, c, idx):
            nonlocal visited
            
            if idx >= len(word): return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]): return False
            if (r,c) in visited: return False
            if board[r][c] != word[idx]: return False
            
            visited.add((r,c))
            
            res = backtrack(r+1, c, idx+1) or backtrack(r-1, c, idx+1) or backtrack(r, c+1, idx+1) or backtrack(r, c-1, idx+1)
        
            visited.remove((r,c))
        
            return res
            
            
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0): 
                        return True
        
        return False