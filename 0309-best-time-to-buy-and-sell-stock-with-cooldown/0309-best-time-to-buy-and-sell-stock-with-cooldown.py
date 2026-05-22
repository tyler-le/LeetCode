class Solution:
    def maxProfit(self, prices: List[int]) -> int:

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

