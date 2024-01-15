class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedily buy low and sell whenever there is a chance for profit
        # [7,1,5,3,4,6] --> 4 + 1 + 2 
        
        buy = prices[0]
        res = 0
        
        for sell in prices[1:]:
            if sell > buy:
                res+=(sell-buy)
            buy = sell
            
        return res
            