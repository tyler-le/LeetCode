class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        OPTIMIZED DP SOLUTION
        Take the DP solution and realize you only track one state back. 
        So keep track of it in single variables.
        """
        buy, sell = -prices[0], 0
        n = len(prices)

        for i in range(n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])
        
        return max(buy,sell)


        """
        DP SOLUTION
        Take the recursive solution (top-down) and convert it to DP (bottom-up)
        """
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


        
        """
        RECURSIVE SOLUTION
        f(index, can_buy) = max profit starting on the ith day with buy or sell
        
        each index, we can either BUY or SELL 

        if we can buy -> profit = max of:
            1.) -prices[i] + f(index + 1, False) --> buy on this day
            2.) 0 + f(index + 1, True) --> can buy but choose not to on this day


        else we can sell -> profit = max of:
            1.) prices[i] + f(index + 1, True) --> sell on this day
            2.) f(index + 1, False) --> can sell but choose not to on this day
        """

        # cache = {}

        # def f(index, can_buy):
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