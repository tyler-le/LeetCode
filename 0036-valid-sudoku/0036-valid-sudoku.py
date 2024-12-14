class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrid = defaultdict(set) # (i, j) pairs

        n, m = len(board), len(board[0])
        EMPTY = "."

        for i in range(n):
            for j in range(m):
                if board[i][j] == ".": continue

                num = int(board[i][j])

                if num in rows[i]: return False
                if num in cols[j]: return False
                if num in subgrid[(i//3,j//3)]: return False

                rows[i].add(num)
                cols[j].add(num)
                subgrid[(i//3, j//3)].add(num)
        
        return True