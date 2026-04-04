class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        # f(i, can_buy) is the max profit starting from day i
        def f(i, can_buy):

            if (i, can_buy) in cache: return cache[(i, can_buy)]

            res = 0

            # base cases
            if i >= n: return 0

            # recursive step
            if can_buy:
                buy = -prices[i] + f(i+1, False)
                hold = 0 + f(i+1, True)
                res = max(buy, hold)
            else:
                sell = prices[i] + f(i+2, True)
                hold = 0 + f(i+1, False)
                res = max(sell, hold)

            cache[(i, can_buy)] = res
            
            return cache[(i, can_buy)]

        return f(0, True)
        