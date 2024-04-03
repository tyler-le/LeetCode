class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx):
            if idx >= len(word): return True
            if i < 0 or j < 0 or i >= n or j >= m: return False
            if word[idx] != board[i][j]: return False
            if (i,j) in visited: return False
            
            visited.add((i,j))
            
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(i+di, j+dj, idx+1):
                    return True
            
            visited.remove((i,j))
            return False
        
        
        n, m = len(board), len(board[0])
        visited = set()
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, 0):
                        return True
        return False