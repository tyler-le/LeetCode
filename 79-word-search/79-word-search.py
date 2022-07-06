class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in path or word[i] != board[r][c]:
                return False
            
            path.add((r,c))
            res =  backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r+1,c,i+1) or backtrack(r,c-1,i+1)
            path.remove((r,c))
            return res
        
        
        rows, cols, path = len(board), len(board[0]), set()
        for row in range(rows):
            for col in range(cols):
                if backtrack(row,col,0):
                    return True
        return False
                
            
        