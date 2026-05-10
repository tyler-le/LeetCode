class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n, m = len(board), len(board[0])

        def dfs(x, y, word_index):

            if word_index >= len(word): return True
            if x < 0 or y < 0 or x >= n or y >= m: return False
            if (x,y) in visited: return False
            if board[x][y] != word[word_index]: return False
            
            visited.add((x,y))

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(x+dx, y+dy, word_index+1):
                    return True

            visited.remove((x,y))

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i,j,0): return True

        return False



        
            