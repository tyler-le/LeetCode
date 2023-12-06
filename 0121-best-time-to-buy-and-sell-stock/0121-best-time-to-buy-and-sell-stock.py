class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if we encounter a smaller number, we have a new buy day
        # treat every day as a sell day
        
        buy_price = float("inf")
        res = 0
        
        for i in range(len(prices)):
    
            if prices[i] < buy_price:
                buy_price = prices[i]
            res = max(res, prices[i] - buy_price)
            
        return res
            