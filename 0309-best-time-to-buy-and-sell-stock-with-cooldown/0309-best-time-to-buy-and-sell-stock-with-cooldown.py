class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)

        @cache
        def rec(index, can_buy):
            res = 0

            if index >= n:
                return 0

            if can_buy:
                buy = -prices[index] + rec(index + 1, False)
                hold = rec(index + 1, True)
                res = max(res, buy, hold)

            else:
                sell = prices[index] + rec(index + 2, True)
                hold = rec(index + 1, False)
                res = max(res, sell, hold)

            return res

        return rec(0, True)

            




