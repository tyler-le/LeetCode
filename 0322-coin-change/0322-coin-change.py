class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        A = [float('inf')] * (amount+1)
        
        A[0] = 0
        print(A)
        for i in range (1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    A[i] = min(A[i], A[i-coin]+1)
                
        return A[amount] if A[amount] != float('inf') else -1
        