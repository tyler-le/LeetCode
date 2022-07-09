class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subgrid = collections.defaultdict(set) # key = (r /3, c /3)
        
        for i in range(9):
            for j in range(9):
                
                curr_num = board[i][j]
                if curr_num == '.':
                    continue
                    
                if curr_num in rows[i] or curr_num in cols[j] or curr_num in subgrid[(i//3,j//3)]:
                    print(rows)

                    return False
                
                rows[i].add(curr_num)
                cols[j].add(curr_num)
                subgrid[(i//3, j//3)].add(curr_num)
                
        return True
                