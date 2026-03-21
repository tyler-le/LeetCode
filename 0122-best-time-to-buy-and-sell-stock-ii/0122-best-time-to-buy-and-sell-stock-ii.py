class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy, sell = -prices[0], 0
        n = len(prices)

        for i in range(n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])
        
        return max(buy,sell)


        
        # n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # BUY_STATE, SELL_STATE = 0, 1

        # dp[0][BUY_STATE] = -prices[0]

        # for i in range(1, n):
        #     buy = -prices[i] + dp[i-1][SELL_STATE]
        #     hold = 0 + dp[i-1][BUY_STATE]
        #     dp[i][BUY_STATE] = max(buy, hold)

        #     sell = prices[i] + dp[i-1][BUY_STATE]
        #     hold = 0 + dp[i-1][SELL_STATE]
        #     dp[i][SELL_STATE] = max(sell, hold) 

        # return max(dp[-1][BUY_STATE], dp[-1][SELL_STATE])


        
        # cache = {}

        # def f(index, can_buy):
        #     # if we can buy 
        #     # -> -prices[i] + f(index + 1, False)
        #     # -> 0 + f(index + 1, True)

        #     # if we cannot buy
        #     # -> prices[i] + f(index + 1, True)
        #     # -> 0 + f(index + 1, False)

        #     if index == len(prices): 
        #         return 0

        #     if (index, can_buy) in cache:
        #         return cache[(index, can_buy)]

        #     if can_buy:
        #         buy = -prices[index] + f(index + 1, False)
        #         hold = 0 + f(index + 1, True)
        #         cache[(index, can_buy)] = max(buy, hold)
        #         return cache[(index, can_buy)]

        #     else:
        #         sell = prices[index] + f(index + 1, True)
        #         hold = 0 + f(index + 1, False)
        #         cache[(index, can_buy)] = max(sell, hold)
        #         return cache[(index, can_buy)]


        # return f(0, True)