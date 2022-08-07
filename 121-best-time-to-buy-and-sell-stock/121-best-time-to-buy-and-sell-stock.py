class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_day = 0
        max_profit = 0
        curr_profit = 0
        for sell_day in range(len(prices)):
            if prices[sell_day] - prices[buy_day] < 0:
                buy_day = sell_day
            else:
                curr_profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, curr_profit)
                
        return max_profit