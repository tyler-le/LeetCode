class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.anti_diag = 0
        

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.board)
        current_player = 1 if player == 1 else -1
            
        self.rows[row]+=current_player
        self.cols[col]+=current_player
        
        if row == col: self.diag+=current_player
            
        if row == n-col-1: self.anti_diag+=current_player
            
        if (abs(self.rows[row]) == n or abs(self.cols[col]) == n 
            or abs(self.diag) == n or abs(self.anti_diag) == n):
            
            return player
        
        return 0
        
        
        
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)