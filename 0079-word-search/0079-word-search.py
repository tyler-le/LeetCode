class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        n = len(word)
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(index, x, y):
            nonlocal rows, cols, visited

            if index == n: return True
            if x < 0 or y < 0 or x >= rows or y >= cols: return False
            if (x,y) in visited: return False
            if word[index] != board[x][y]: return False

            visited.add((x,y))
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r, c = x+dx, y+dy
                if backtrack(index + 1, r, c):
                    return True
            
            visited.remove((x,y))
            

            return False

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(0, r, c):
                    return True
        
        return False