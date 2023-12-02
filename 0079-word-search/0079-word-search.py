class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = set()
        
        def backtrack(x, y, word):
            if x < 0 or y < 0 or x >= n or y >= m: return False
            if (x, y) in visited: return False
            if len(word) == 1 and board[x][y] == word[0]: return True
            if board[x][y] != word[0]: return False
            
            visited.add((x,y))
            res = backtrack(x+1, y, word[1:]) or backtrack(x-1, y, word[1:]) or backtrack(x, y+1, word[1:]) or backtrack(x, y-1, word[1:])
            visited.remove((x,y))
            
            return res
     
            
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, word): 
                    return True
        return False
