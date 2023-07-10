class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n,m = len(board), len(board[0])
        
        def backtrack(i, j, word):

            if i < 0 or j < 0 or i >= n or j >= m or (i,j) in visited:
                return False
            
            if len(word) == 0:
                return True
            
            if len(word) == 1 and word[0] == board[i][j]:
                return True
            
            if board[i][j] != word[0]:
                return False
            
            visited.add((i,j))
            
            res = backtrack(i+1, j, word[1:]) or backtrack(i-1, j, word[1:]) or backtrack(i, j+1, word[1:]) or backtrack(i, j-1, word[1:])
            
            visited.remove((i,j))
            
            return res
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, word): return True
        return False
            