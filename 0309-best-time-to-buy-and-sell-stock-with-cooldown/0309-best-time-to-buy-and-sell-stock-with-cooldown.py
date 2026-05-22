class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+2)]
        can_buy, cannot_buy = 0, 1


        for i in range(n - 1, -1, -1):
            buy = -prices[i] + dp[i+1][cannot_buy]
            hold = dp[i + 1][can_buy]
            dp[i][can_buy] = max(dp[i][can_buy], buy, hold)

            sell = prices[i] + dp[i+2][can_buy]
            hold = dp[i+1][cannot_buy]
            dp[i][cannot_buy] = max(dp[i][cannot_buy], sell, hold)

        return dp[0][can_buy]
            


        n = len(prices)
        @cache
        def f(index, can_buy):
            if index >= n: return 0

            res = 0

            if can_buy:
                buy = -prices[index] + f(index + 1, False)
                hold = f(index + 1, True)
                res = max(res, buy, hold)
            else:
                sell = prices[index] + f(index + 2, True)
                hold = f(index + 1, False)
                res = max(res, sell, hold)

            return res

        return f(0, True)

