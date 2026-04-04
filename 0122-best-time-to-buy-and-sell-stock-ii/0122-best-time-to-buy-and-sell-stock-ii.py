class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedily buy (low) and sell (high)

        res = 0
        n = len(prices)
        buy_price = math.inf

        for i in range(n):

            # greedily buy low
            if buy_price > prices[i]:
                buy_price = prices[i]

            # encounter a good day to sell (buy < sell)
            else:
                res+=prices[i] - buy_price
                buy_price = prices[i]
        
        return res
