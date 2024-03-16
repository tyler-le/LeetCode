class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # hash map problem
        rows = defaultdict(set)
        cols = defaultdict(set)
        section = defaultdict(set)
        
        n, m = len(board), len(board[0])
        
        for i in range(n):
            for j in range(m):
                curr = board[i][j]
                if curr == '.': 
                    continue
                if curr in rows[i] or curr in cols[j] or curr in section[(i//3, j//3)]:
                    return False
                
                rows[i].add(curr)
                cols[j].add(curr)
                section[(i//3, j//3)].add(curr)
                
        return True
                