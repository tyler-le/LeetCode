class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF] * (amount+1)
        dp[0] = 0
        
        for amt in range (1, amount+1):
            for coin in coins:
                if amt - coin < 0: continue
                dp[amt] = min(dp[amt], dp[amt-coin]+1)

        return dp[-1] if dp[-1] != INF else -1