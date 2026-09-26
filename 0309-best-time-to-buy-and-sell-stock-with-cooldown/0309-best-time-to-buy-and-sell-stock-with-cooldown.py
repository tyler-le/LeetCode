class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def f(index, can_buy):
            res = 0

            # base case
            if index >= len(prices): return 0

            # recursive calls
            if can_buy:
                buy = -prices[index] + f(index + 1, False)
                hold = f(index + 1, True)
                res = max(buy, hold)
            else:
                sell = prices[index] + f(index + 2, True)
                hold = f(index + 1, False)
                res = max(sell, hold)
            
            return res

        return f(0, True)