class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def f(index, can_buy):
            # if we can buy 
            # -> -prices[i] + f(index + 1, False)
            # -> 0 + f(index + 1, True)

            # if we cannot buy
            # -> prices[i] + f(index + 1, True)
            # -> 0 + f(index + 1, False)

            if index == len(prices): 
                return 0

            if (index, can_buy) in cache:
                return cache[(index, can_buy)]

            if can_buy:
                buy = -prices[index] + f(index + 1, False)
                hold = 0 + f(index + 1, True)
                cache[(index, can_buy)] = max(buy, hold)
                return cache[(index, can_buy)]

            else:
                sell = prices[index] + f(index + 1, True)
                hold = 0 + f(index + 1, False)
                cache[(index, can_buy)] = max(sell, hold)
                return cache[(index, can_buy)]


        return f(0, True)