class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_profit = 0
        buy_day = prices[0]
        
        for price in prices:
            curr_profit = price - buy_day
            res = max(res, curr_profit)
            if price < buy_day:
                buy_day = price
        
        return res
            
            