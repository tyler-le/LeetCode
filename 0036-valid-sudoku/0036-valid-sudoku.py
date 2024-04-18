class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hashmap of sets
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrid = defaultdict(set) 
        
        n, m = len(board), len(board[0])
        
        for i in range(n):
            for j in range(m):
                elem = board[i][j]
                
                if elem == ".": continue
                if elem in rows[i] or elem in cols[j] or elem in subgrid[(i//3, j//3)]:
                    return False
                
                rows[i].add(elem)
                cols[j].add(elem)
                subgrid[(i//3,j//3)].add(elem)
        
        return True
                
                
                    
        
        