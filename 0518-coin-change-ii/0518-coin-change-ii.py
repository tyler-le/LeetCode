class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        A = [[1]+[0]*amount for _ in range(len(coins)+1)]
            
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0: IN = A[i][j-coins[i-1]]
                else: IN = 0
                OUT = A[i-1][j]
                A[i][j] = IN + OUT

        return A[-1][-1]
        