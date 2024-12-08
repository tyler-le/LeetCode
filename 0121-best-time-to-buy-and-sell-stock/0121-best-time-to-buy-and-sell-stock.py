class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_profit = 0
        bought_price = prices[0]
        
        for price in prices:
            if price < bought_price:
                bought_price = price
                
            curr_profit = price - bought_price
            res = max(res, curr_profit)
            
        return res
            
            