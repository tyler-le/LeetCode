class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # map (i,j) : num_live
        hmap, rows, cols = collections.defaultdict(int), len(board), len(board[0])
        
        
        def num_neighbors_live(i, j):
            res = 0
            # check above
            if i > 0: res+= board[i-1][j]
            
            # check left
            if j > 0: res+=board[i][j-1]
                
            # check right:
            if j < cols-1: res+=board[i][j+1]
        
            # check down
            if i < rows-1: res+=board[i+1][j]
                
            # check top-left diag
            if i > 0 and j > 0: res+=board[i-1][j-1]
            
            # check bottom-right diag
            if i < rows-1 and j < cols-1: res+=board[i+1][j+1]
            
            # check bottom-left diag
            if i < rows-1 and j > 0: res+=board[i+1][j-1]
            
            # check top-right diag
            if i > 0 and j < cols-1: res+=board[i-1][j+1]
                
            return res
        
        
        # get the number of alive neighbors and map (i,j) : # live neighbors
        for i in range(rows):
            for j in range(cols):
                hmap[(i,j)] = num_neighbors_live(i, j)
                               
        # second pass through board and kill/live based on conditions
        for i in range(rows):
            for j in range(cols):
                num_live_neighbors = hmap[(i, j)]
                if board[i][j] == 0:
                    if num_live_neighbors == 3: 
                        board[i][j] = 1
                
                elif board[i][j] == 1:
                    if num_live_neighbors < 2: board[i][j] = 0
                    elif 2 <= num_live_neighbors <= 3: board[i][j] = 1
                    elif num_live_neighbors > 3: board[i][j] = 0
                    
                    