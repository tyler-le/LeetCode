class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        # player1 -> +1
        # player2 -> -1
        curr_player = 1 if player == 1 else -1
        n = self.n
        
        self.rows[row]+=curr_player
        self.cols[col]+=curr_player
        if row == col: self.diag+=curr_player
        if (row) == (n - col - 1): self.anti_diag+=curr_player
        if (abs(self.rows[row]) == n or abs(self.cols[col]) == n 
            or abs(self.diag) == n or abs(self.anti_diag) == n):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)