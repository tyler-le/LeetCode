class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_day, sell_day = 0, 1
        curr_profit, max_profit = 0, 0
        
        while sell_day < len(prices):
            
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
                sell_day += 1
                curr_profit = 0
                
            else:
                curr_profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, curr_profit)
                sell_day += 1
                
        return max_profit