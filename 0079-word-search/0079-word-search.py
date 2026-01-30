class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])

        def backtrack(x, y, index, visited):

            nonlocal n, m

            # base case
            if word[index] != board[x][y]: return False
            if index == len(word) - 1: return True

            # recursive step
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = x + dx
                c = y + dy

                if r < 0 or c < 0 or r >= n or c >= m: continue
                if (r,c) in visited: continue

                visited.add((r, c))
                if backtrack(r, c, index+1, visited): return True
                visited.remove((r, c))

            return False

        for i in range(n):
            for j in range(m):
                visited = set()
                visited.add((i,j))

                if backtrack(i, j, 0, visited): return True
        
        return False